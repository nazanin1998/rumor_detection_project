from lib.preprocessing.pheme.expand_contactions.expand_contractions_impl import ExpandContractionsImpl
from lib.preprocessing.pheme.remove_username.remove_username_impl import RemoveUsernameImpl
from lib.preprocessing.pheme.special_characters_removal.special_char_removal_impl import SpecialCharacterRemovalImpl
from lib.preprocessing.pheme.stop_word_removal.stop_word_removal_impl import StopWordRemovalImpl
from lib.preprocessing.pheme.tokenizing.tokenizing_impl import TokenizingImpl
from lib.preprocessing.pheme.word_root.word_root_lemmatization_impl import WordRootLemmatizationImpl
from os import environ as env
import lib.constants as constants

from lib.read_datasets.pheme.file_dir_handler import FileDirHandler


class PreProcessing:
    def __init__(self, df):
        self.df = df
        self.i = 0
        preprocess_dir = FileDirHandler.read_directories(directory=constants.PHEME_PRE_PROCESS_CSV_DIR)

        if preprocess_dir is None or not preprocess_dir.__contains__(constants.PHEME_PRE_PROCESS_CSV_NAME):
            self.preprocess()
        else:
            self.read_preprocessed_csv_dataset()

    def preprocess(self):
        self.df['user.description'] = self.df['user.description'].apply(
            lambda x: self.__preprocess(x))
        self.df.to_csv(constants.PHEME_PRE_PROCESS_CSV_PATH, index=False)
        self.df['text'] = self.df['text'].apply(
            lambda x: self.__preprocess(x))
        self.df.to_csv(constants.PHEME_PRE_PROCESS_CSV_PATH, index=False)

    def __preprocess(self, text):
        self.i += 1
        print(self.i, end=', ')
        self.expanded_text = ExpandContractionsImpl().expand(text=text)

        self.text_without_username = RemoveUsernameImpl().remove_usernames(text=self.expanded_text)
        self.text_without_links, links = RemoveUsernameImpl().remove_links(text=self.text_without_username)
        self.text_without_emails, emails = RemoveUsernameImpl().remove_emails(text=self.text_without_links)

        self.tokens = TokenizingImpl().tokenize(sentence=self.text_without_emails)

        self.words_roots = WordRootLemmatizationImpl().find_batch_words_root(tokens=self.tokens)

        self.tokens_without_sw = StopWordRemovalImpl().remove(tokens=self.words_roots)

        self.tokens_without_sc = SpecialCharacterRemovalImpl().remove(tokens=self.tokens_without_sw)

        self.sentence = self.tokens_to_sentence(tokens=self.tokens_without_sc, links=links, emails=emails)
        self.sentence = self.sentence.lower()
        self.print_summery()
        return self.sentence

    def read_preprocessed_csv_dataset(self):
        print("Read Preprocessed CSV Dataset ...", end=' => ')
        self.df = FileDirHandler.read_csv_file(path=constants.PHEME_PRE_PROCESS_CSV_PATH)
        print(self.df.shape)

    @staticmethod
    def tokens_to_sentence(tokens, emails, links):
        if tokens is None:
            return ''
        sentence = ''
        for token in tokens:
            sentence = sentence + ' ' + token
        if emails is not None:
            for email in emails:
                sentence = sentence + ' ' + email
        if links is not None:
            for link in links:
                sentence = sentence + ' ' + link
        sentence = sentence.strip()
        return sentence

    def print_summery(self):
        print("1 => expanded_text")
        print(self.expanded_text)
        # print("2 => text_without_username")
        # print(self.text_without_username)
        # print("3 => tokens")
        # print(self.tokens)
        # print("4 => words_roots")
        # print(self.words_roots)
        # print("5 => tokens_without_sw")
        # print(self.tokens_without_sw)
        # print("6 => tokens_without_sc")
        # print(self.tokens_without_sc)
        print("7 => sentence")
        print(self.sentence)

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
