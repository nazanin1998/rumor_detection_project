import os
import pandas as pd

import lib.constants as constants
from lib.models.event_model import EventModel
from lib.models.tweet import Tweet
from lib.models.tweet_tree import TweetTree
from lib.read_datasets.pheme.json_helper import read_json_file


class ReadPhemeDataset:
    def __init__(self, path):
        self.path = path
        self.events = None
        self.df = None

    def read_json_dataset(self):
        print("Read Json Dataset ...", end=' => ')
        self.events = self.__extract_events_from_dataset()
        self.__extract_csv_from_events()
        print(self.df.shape)

    def read_csv_dataset(self):
        print("Read CSV Dataset ...", end=' => ')
        self.df = pd.read_csv(constants.PHEME_CSV_PATH, lineterminator='\n')
        print(self.df.shape)

    def read_preprocessed_csv_dataset(self):
        print("Read Preprocessed CSV Dataset ...", end=' => ')
        self.df = pd.read_csv(constants.PHEME_PRE_PROCESS_CSV_PATH, lineterminator='\n')
        print(self.df.shape)

    def print_summery(self):
        index = 0
        for event in self.events:
            index += 1
            print(event.to_string(index=index))

    def __extract_events_from_dataset(self):
        events = []
        event_dirs = self.__read_directories(path=self.path)

        for event_dir in event_dirs:
            inner_event_dirs = self.__read_directories(path=self.path + event_dir)
            if inner_event_dirs is None:
                continue

            event = EventModel(path=event_dir, rumors=[], non_rumors=[])
            for inner_event_dir in inner_event_dirs:
                if inner_event_dir == constants.NON_RUMOURS:
                    event.non_rumors = self._tweet_trees_extraction(event_dir, inner_event_dir)
                elif inner_event_dir == constants.RUMOURS:
                    event.rumors = self._tweet_trees_extraction(event_dir, inner_event_dir)
            events.append(event)
        return events

    def __extract_csv_from_events(self):
        tweets = self._extract_tweet_list_from_events()
        self.df = pd.DataFrame(tweets)

        os.makedirs(constants.PHEME_CSV_DIR, exist_ok=True)
        self.df.to_csv(constants.PHEME_CSV_PATH, index=False)

    def _extract_tweet_list_from_events(self):
        tweets = []
        for event in self.events:

            for rumour in event.rumors:
                tweets.append(rumour.source_tweet.to_json(is_rumour=0, event=event.name, is_source_tweet=0))
                for reaction in rumour.reactions:
                    tweets.append(reaction.to_json(is_rumour=0, event=event.name, is_source_tweet=1))

            for non_rumour in event.non_rumors:
                tweets.append(non_rumour.source_tweet.to_json(is_rumour=1, event=event.name, is_source_tweet=0))
                for reaction in non_rumour.reactions:
                    tweets.append(reaction.to_json(is_rumour=1, event=event.name, is_source_tweet=1))

        return tweets

    def _tweet_trees_extraction(self, event_dir, inner_event_dir):
        tweet_trees = []

        base_path = self.path + event_dir + '/' + inner_event_dir
        tweet_trees_dirs = self.__read_directories(path=base_path)

        if tweet_trees_dirs is None:
            return None

        for tweet_tree_id in tweet_trees_dirs:
            tweet_tree_path = base_path + '/' + tweet_tree_id
            source_tweet_path = tweet_tree_path + '/source-tweets/' + tweet_tree_id + '.json'
            reactions_path = tweet_tree_path + '/reactions/'

            source_tweet_obj = self._tweet_file_to_obj(source_tweet_path)
            reaction_file_paths = self.__read_directories(reactions_path)

            reactions = []
            if reaction_file_paths is None:
                continue
            for reaction_file_path in reaction_file_paths:
                reaction_path = reactions_path + reaction_file_path
                reactions.append(self._tweet_file_to_obj(reaction_path))

            tweet_trees.append(TweetTree(source_tweet=source_tweet_obj, reactions=reactions))
        return tweet_trees

    @staticmethod
    def _tweet_file_to_obj(path):
        tweet_json_obj = read_json_file(path)
        if tweet_json_obj is None:
            return None
        return Tweet.from_json(tweet_json_obj)

    def __read_directories(self, path=None):
        try:
            if path is None:
                path = self.path
            return os.listdir(path)
        except:
            return None

    @staticmethod
    def read_directories(path):
        try:
            return os.listdir(path)
        except:
            return None
