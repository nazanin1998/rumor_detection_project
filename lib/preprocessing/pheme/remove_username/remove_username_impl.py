from lib.preprocessing.pheme.remove_username.remove_username import RemoveUsername
import re


class RemoveUsernameImpl(RemoveUsername):
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
            return None

        emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
        for email in emails:
            text = str(text).replace(email, '')
        return text, emails

    def remove_links(self, text):
        if text is None:
            return None

        urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', text)
        for url in urls:
            text = str(text).replace(url, '')
        return text, urls
