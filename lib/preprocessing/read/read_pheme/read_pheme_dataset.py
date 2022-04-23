import os

from lib.models.event_model import EventModel
from lib.models.tweet import Tweet
from lib.models.tweet_tree import TweetTree
from lib.preprocessing.read.read_pheme.json_helper import read_json_file


class ReadPhemeDataset:
    def __init__(self, path):
        self.path = path
        self.__read_inner_event_directories()

    def __read_inner_event_directories(self):
        event_dirs = self.__read_directories()
        events = []
        for event_dir in event_dirs:
            inner_event_dirs = self.__read_directories(partial_path=event_dir)
            if inner_event_dirs is None:
                continue

            print('EVENT => ' + event_dir)

            event_item = EventModel(path=event_dir, rumors=[], non_rumors=[])
            for inner_event_dir in inner_event_dirs:
                if inner_event_dir == 'non-rumours':
                    non_rumor_tweet_trees = self._tweet_trees_extraction(event_dir, inner_event_dir)
                    event_item.non_rumors = non_rumor_tweet_trees
                    print('\tnon-rumor-len is : ' + str(len(non_rumor_tweet_trees)))
                elif inner_event_dir == 'rumours':
                    rumor_tweet_trees = self._tweet_trees_extraction(event_dir, inner_event_dir)
                    event_item.rumors = rumor_tweet_trees
                    print('\trumor-len is : ' + str(len(rumor_tweet_trees)))
            events.append(event_item)
        print(len(events))

    def _tweet_trees_extraction(self, event_dir, inner_event_dir):
        pre_path = event_dir + '/' + inner_event_dir
        tweet_trees_dirs = self.__read_directories(partial_path=pre_path)
        tweet_trees = []

        if tweet_trees_dirs is None:
            return None
        for tweet_tree_id in tweet_trees_dirs:
            tweet_tree_path = pre_path + '/' + tweet_tree_id
            source_tweet_path = self.path + tweet_tree_path + '/source-tweets/' + tweet_tree_id + '.json'
            source_tweet_obj = self._tweet_file_to_obj(source_tweet_path)
            reactions_path = tweet_tree_path + '/reactions/'
            reaction_file_paths = self.__read_directories(reactions_path)

            reactions = []
            if reaction_file_paths is None:
                continue
            for reaction_file_path in reaction_file_paths:
                reaction_path = self.path + reactions_path + reaction_file_path
                reactions.append(self._tweet_file_to_obj(reaction_path))

            tweet_trees.append(TweetTree(source_tweet=source_tweet_obj, reactions=reactions))
        return tweet_trees

    @staticmethod
    def _tweet_file_to_obj(path):
        tweet_json_obj = read_json_file(path)
        if tweet_json_obj is None:
            return None
        return Tweet.from_json(tweet_json_obj)

    def __read_directories(self, partial_path=''):
        try:
            return os.listdir(self.path + partial_path)
        except:
            return None
