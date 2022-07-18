from nltk.corpus import stopwords

from lib.preprocessing.pheme.stop_word_removal.stop_word_removal import StopWordRemoval


class StopWordRemovalImpl(StopWordRemoval):
    def remove(self, tokens):
        tokens_without_sw = [word for word in tokens if not word in stopwords.words()]
        return tokens_without_sw
