import numpy

from lib.preprocessing.pheme.bert_embedding.bert_embedding_impl2 import BertEmbeddingImpl2
from lib.preprocessing.pheme.expand_contactions.expand_contractions_impl import ExpandContractionsImpl
from lib.preprocessing.pheme.remove_username.remove_username_impl import RemoveUsernameImpl
from lib.preprocessing.pheme.special_characters_removal.special_char_removal_impl import SpecialCharacterRemovalImpl
from lib.preprocessing.pheme.stop_word_removal.stop_word_removal_impl import StopWordRemovalImpl
from lib.preprocessing.pheme.tokenizing.tokenizing_impl import TokenizingImpl
# from lib.preprocessing.pheme.tokenizing.tokenizing_impl_bert import TokenizingImplBert
from lib.preprocessing.pheme.word_root.word_root_lemmatization_impl import WordRootLemmatizationImpl
import lib.constants as constants

from lib.read_datasets.pheme.file_dir_handler import FileDirHandler

# //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
class PreProcessing:
    def __init__(self, df):
        print("\n<< PHASE-2: PREPROCESS >>")
        self.df = df
        self.i = 0
        preprocess_dir = FileDirHandler.read_directories(directory=constants.PHEME_PRE_PROCESS_CSV_DIR)

        if preprocess_dir is None or not preprocess_dir.__contains__(constants.PHEME_PRE_PROCESS_CSV_NAME):
            self.preprocess()
        else:
            self.read_preprocessed_csv_dataset()
        print("<< PHASE-2: PREPROCESS DONE>>")

    def preprocess(self):
        self.df['user.description'] = self.df['user.description'].apply(
            lambda x: self.__preprocess(x))
        self.df.to_csv(constants.PHEME_PRE_PROCESS_CSV_PATH, index=False)
        self.df['text'] = self.df['text'].apply(
            lambda x: self.__preprocess(x))
        self.df.to_csv(constants.PHEME_PRE_PROCESS_CSV_PATH, index=False)

    def __preprocess(self, text):
        self.i += 1
        print(self.i)
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
        self.embed = BertEmbeddingImpl2().bert_embed(self.sentence)
        # self.print_summery()
        if self.embed is None:
            return numpy.NaN
        return self.embed

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
        print("\n1 => expanded_text")
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
