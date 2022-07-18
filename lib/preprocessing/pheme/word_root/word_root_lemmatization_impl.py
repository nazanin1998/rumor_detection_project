from nltk import WordNetLemmatizer
from lib.preprocessing.pheme.word_root.word_root import WordRoot


class WordRootLemmatizationImpl(WordRoot):
    def find_batch_words_root(self, tokens):
        wordnet_lemmatizer = WordNetLemmatizer()

        lemma_tokens = []
        for w in tokens:
            value = wordnet_lemmatizer.lemmatize(w, pos="v")
            lemma_tokens.append(value)
        return lemma_tokens


