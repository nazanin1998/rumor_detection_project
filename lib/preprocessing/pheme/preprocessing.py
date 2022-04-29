import io
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from lib.models.event_model import EventModel


class PreProcessing:
    def __init__(self, events):
        self.events = events

    # def preprocess(self):
        # self.__extract_usefull_data()
        # self.__tokenizing()

    # def __tokenizing(self):
    #     stop_words = set(stopwords.words('english'))
    #
    #     for event in self.events:
    #         for tweet_tree in event.rumours:
    #             text,
    #     # words = line.split()
    #     # for r in words:
    #     #     if not r in stop_words:
    #     #         appendFile = open('filteredtext.txt', 'a')
    #     #         appendFile.write(" " + r)
    #     #         appendFile.close()
