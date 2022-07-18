from lib.preprocessing.pheme.expand_contactions.expand_contractions_impl import ExpandContractionsImpl
from lib.preprocessing.pheme.remove_username.remove_username_impl import RemoveUsernameImpl
from lib.preprocessing.pheme.special_characters_removal.special_char_removal_impl import SpecialCharacterRemovalImpl
from lib.preprocessing.pheme.stop_word_removal.stop_word_removal_impl import StopWordRemovalImpl
from lib.preprocessing.pheme.tokenizing.tokenizing_impl import TokenizingImpl
from lib.preprocessing.pheme.word_root.word_root_lemmatization_impl import WordRootLemmatizationImpl


class PreProcessing:
    def __init__(self, df):
        self.df = df
        self.i = 0

    def preprocess(self):
        self.__preprocess('@AP plus 1 Turkish citizen..')
        self.__preprocess(
            '@AP @FAANews @AirportKRAL An automated sys should be installed that takes command of the acft if it goes off course for x amount of time')
        # self.df['text'] = self.df['text'].apply(
        #     lambda x: self.__preprocess(x))
        # self.df.to_csv('./dataset/pheme_csv/pheme_preprocess_lemmatization.csv', index=False)

    def __preprocess(self, text):
        self.i += 1
        print(self.i, end=', ')
        expanded_text = ExpandContractionsImpl().expand(text=text)

        text_without_username = RemoveUsernameImpl().remove(text=expanded_text)

        tokens = TokenizingImpl().tokenize(sentence=text_without_username)

        words_roots = WordRootLemmatizationImpl().find_batch_words_root(tokens=tokens)

        tokens_without_sw = StopWordRemovalImpl().remove(tokens=words_roots)

        tokens_without_sc = SpecialCharacterRemovalImpl().remove(tokens=tokens_without_sw)

        sentence = self.tokens_to_sentence(tokens_without_sc)
        sentence = sentence.lower()

        return sentence

    @staticmethod
    def tokens_to_sentence(tokens):
        sentence = ''
        for token in tokens:
            sentence = sentence + ' ' + token
        sentence = sentence.strip()
        return sentence

    def remove_redundant_information(self):
        print('remove_redundant_information')

    def convert_accented_characters_to_ASCIIs(self):
        print('convert_accented_characters_to_ASCIIs')

    def noise_removal(self):
        print('Noise Removal')

    def normalization(self):
        print('normalization')
    # def remove_username(self, text):
    #     split_texts = text.split(' ')
    #     text_without_username = ''
    #     for split_text in split_texts:
    #         if not split_text.startswith("@"):
    #             text_without_username = text_without_username + ' ' + split_text
    #     return text_without_username

    # def stemming(self, tokens):
    #     ps = PorterStemmer()
    #
    #     stemmed_tokens = []
    #     for w in tokens:
    #         value = ps.stem(w)
    #         stemmed_tokens.append(value)
    #     return stemmed_tokens

    # def lemmatization(self, tokens):
    #     wordnet_lemmatizer = WordNetLemmatizer()
    #
    #     lemma_tokens = []
    #     for w in tokens:
    #         value = wordnet_lemmatizer.lemmatize(w, pos="v")
    #         lemma_tokens.append(value)
    #     return lemma_tokens

    # @staticmethod
    # def remove_special_characters(tokens):
    #     tokens_without_special_char = []
    #     for token in tokens:
    #         if str(''.join(filter(str.isalnum, token))) != '':
    #             tokens_without_special_char.append(''.join(filter(str.isalnum, token)))
    #     return tokens_without_special_char

    # @staticmethod
    # def tokenizing(text):
    #     tokenizer = BertTokenizer(vocab_file='./vocab.txt')
    #     tokens = tokenizer.tokenize(text)
    #     return tokens

    # @staticmethod
    # def stop_word_removal(tokens):
    #     tokens_without_sw = [word for word in tokens if not word in stopwords.words()]
    #     return tokens_without_sw

    # def expand_contractions(self, text):
    #     expanded_words = []
    #     for word in text.split():
    #         try:
    #             expanded_words.append(contractions.fix(word))
    #         except:
    #             print("baby", end=' ')
    #             print(word, end=' ')
    #             break
    #
    #     return ' '.join(expanded_words)
