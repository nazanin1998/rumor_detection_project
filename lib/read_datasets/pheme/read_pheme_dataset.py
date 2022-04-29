import os
import pandas as pd
from lib.models.event_model import EventModel
from lib.models.tweet import Tweet
from lib.models.tweet_tree import TweetTree
from lib.read_datasets.pheme.json_helper import read_json_file


class ReadPhemeDataset:
    def __init__(self, path):
        self.path = path
        self.events = self.__read_inner_event_directories()
        self.__extract_useful_data()

    def __extract_useful_data(self):
        tweets = []
        for event in self.events:
            for rumour in event.rumors:
                src_tweet_json = rumour.source_tweet.to_json(is_rumour=0, event=event.name, is_source_tweet=0)
                tweets.append(src_tweet_json)
                for reaction in rumour.reactions:
                    reaction_json = reaction.to_json(is_rumour=0, event=event.name, is_source_tweet=1)
                    tweets.append(reaction_json)
        tweets_dataframes = pd.DataFrame(tweets)

        print("after extract useful data")
        print(tweets_dataframes.shape)
        import os
        os.makedirs('folder/subfolder', exist_ok=True)
        tweets_dataframes.to_csv('folder/subfolder/out.csv', index=False)
        # tweets_dataframes.to_csv(index=False)


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
        return events

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
