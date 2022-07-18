from lib.preprocessing.pheme.remove_username.remove_username import RemoveUsername


class RemoveUsernameImpl(RemoveUsername):
    def remove(self, text):
        split_texts = text.split(' ')
        text_without_username = ''
        for split_text in split_texts:
            if not split_text.startswith("@"):
                text_without_username = text_without_username + ' ' + split_text
        return text_without_username
