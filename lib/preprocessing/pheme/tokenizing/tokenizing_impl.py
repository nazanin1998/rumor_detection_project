from transformers import BertTokenizer

from lib.preprocessing.pheme.tokenizing.tokenizing import Tokenizing


class TokenizingImpl(Tokenizing):
    def tokenize(self, sentence):
        tokenizer = BertTokenizer(vocab_file='./vocab.txt')
        tokens = tokenizer.tokenize(sentence)
        return tokens
