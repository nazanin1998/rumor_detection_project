from lib.preprocessing.pheme.remover.remover import Remover
import re
from nltk.corpus import stopwords


class RemoverImpl(Remover):

    def __init__(self):
        self.stop_words = stopwords.words()

    def remove_usernames(self, text):
        if text is None:
            return None
        split_texts = text.split(' ')
        text_without_username = ''
        for split_text in split_texts:
            if not split_text.startswith("@"):
                text_without_username = text_without_username + ' ' + split_text
        return text_without_username

    def remove_emails(self, text):
        if text is None:
            return None, None

        emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
        for email in emails:
            text = str(text).replace(email, '')
        return text, emails

    def remove_links(self, text):
        if text is None:
            return None, None

        urls = re.findall(r'(https?://\S+)', text)
        for url in urls:
            text = str(text).replace(url, '')
        return text, urls

    def remove_stop_words(self, tokens):
        if tokens is None:
            return None
        tokens_without_sw = [word for word in tokens if not word in self.stop_words]
        return tokens_without_sw

    def remove_special_characters(self, tokens):
        if tokens is None:
            return None
        tokens_without_special_char = []
        for token in tokens:
            if str(''.join(filter(str.isalnum, token))) != '':
                tokens_without_special_char.append(''.join(filter(str.isalnum, token)))
        return tokens_without_special_char

