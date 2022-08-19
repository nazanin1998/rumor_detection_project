from transformers import TFBertTokenizer


from transformers import BertTokenizer

from lib.preprocessing.pheme.tokenizing.tokenizing import Tokenizing


class TokenizingImplBert(Tokenizing):
    def tokenize(self, sentence):
        if sentence is None:
            return None
        print("baby")
        # tf_tokenizer = TFBertTokenizer.from_pretrained("bert-base-uncased")
        # print("baby")

        # encoding = tf_tokenizer.encode(sentence)
        # print(encoding)
        # tokens = tf_tokenizer.convert_ids_to_tokens(encoding)

        tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
        tokens = tokenizer(sentence, return_tensors="pt")
        print("tokens")
        print(tokens)
        # tokenizer = BertTokenizer(vocab_file='./vocab.txt')
        # tokens = tokenizer.tokenize(sentence)
        return tokens
