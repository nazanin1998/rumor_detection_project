from nltk.corpus import stopwords
from transformers import BertTokenizer
from nltk.stem import PorterStemmer
import contractions


class PreProcessing:
    def __init__(self, df):
        self.df = df
        self.i = 0

    def preprocess(self):
        self.df['text'] = self.df['text'].apply(
            lambda x: self.__preprocess(x))
        self.df.to_csv('./dataset/pheme_csv/pheme_preprocess3.csv', index=False)

    def __preprocess(self, text):
        self.i += 1
        print(self.i, end=', ')

        expanded_text = self.expand_contractions(text)
        text_without_username = self.remove_username(expanded_text)
        tokens = self.tokenizing(text_without_username)

        stemmed_tokens = self.stemming(tokens)
        tokens_without_sw = self.stop_word_removal(stemmed_tokens)
        tokens_without_sc = self.remove_special_characters(tokens_without_sw)
        sentence = self.tokens_to_sentence(tokens_without_sc)
        sentence = sentence.lower()
        return sentence

    def remove_username(self, text):
        split_texts = text.split(' ')
        text_without_username = ''
        for split_text in split_texts:
            if not split_text.startswith("@"):
                text_without_username = text_without_username + ' ' + split_text
        return text_without_username

    def stemming(self, tokens):
        ps = PorterStemmer()

        stemmed_tokens = []
        for w in tokens:
            value = ps.stem(w)
            stemmed_tokens.append(value)
        return stemmed_tokens

    @staticmethod
    def remove_special_characters(tokens):
        tokens_without_special_char = []
        for token in tokens:
            if str(''.join(filter(str.isalnum, token))) != '':
                tokens_without_special_char.append(''.join(filter(str.isalnum, token)))
        return tokens_without_special_char

    @staticmethod
    def tokens_to_sentence(tokens):
        sentence = ''
        for token in tokens:
            sentence = sentence + ' ' + token
        sentence = sentence.strip()
        return sentence

    @staticmethod
    def tokenizing(text):
        tokenizer = BertTokenizer(vocab_file='./vocab.txt')
        tokens = tokenizer.tokenize(text)
        return tokens

    @staticmethod
    def stop_word_removal(tokens):
        tokens_without_sw = [word for word in tokens if not word in stopwords.words()]
        return tokens_without_sw

    def remove_redundant_information(self):
        print('remove_redundant_information')

    def convert_accented_characters_to_ASCIIs(self):
        print('convert_accented_characters_to_ASCIIs')

    def expand_contractions(self, text):
        expanded_words = []
        for word in text.split():
            try:
                expanded_words.append(contractions.fix(word))
            except:
                print("baby", end=' ')
                print(word, end=' ')
                break

        return ' '.join(expanded_words)

    def noise_removal(self):
        print('Noise Removal')

    def normalization(self):
        print('normalization')
