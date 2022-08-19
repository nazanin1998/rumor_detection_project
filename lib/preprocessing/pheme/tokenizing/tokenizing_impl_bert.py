from transformers import TFBertTokenizer


from transformers import BertTokenizer

from lib.preprocessing.pheme.tokenizing.tokenizing import Tokenizing


class TokenizingImplBert(Tokenizing):
    def tokenize(self, sentence):
        if sentence is None:
            return None
        print("baby")
        tf_tokenizer = TFBertTokenizer.from_pretrained("bert-base-uncased")
        print("baby")
        tokens = tf_tokenizer(sentence)
        print("tokens")
        print(tokens)
        # tokenizer = BertTokenizer(vocab_file='./vocab.txt')
        # tokens = tokenizer.tokenize(sentence)
        return tokens
