from nltk.stem import PorterStemmer

from lib.preprocessing.pheme.word_root.word_root import WordRoot


class WordRootStemmingImpl(WordRoot):
    def find_batch_words_root(self, tokens):
        ps = PorterStemmer()

        stemmed_tokens = []
        for w in tokens:
            value = ps.stem(w)
            stemmed_tokens.append(value)
        return stemmed_tokens
