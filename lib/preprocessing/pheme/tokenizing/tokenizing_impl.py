from transformers import BertTokenizer

from lib.preprocessing.pheme.tokenizing.tokenizing import Tokenizing


class TokenizingImpl(Tokenizing):
    def __init__(self):
        self.tokenizer = BertTokenizer(vocab_file='./vocab.txt')

    def tokenize(self, sentence):
        if sentence is None:
            return None

        tokens = self.tokenizer.tokenize(sentence)
        return tokens
