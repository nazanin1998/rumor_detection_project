from lib.preprocessing.pheme.special_characters_removal.special_char_removal import SpecialCharacterRemoval


class SpecialCharacterRemovalImpl(SpecialCharacterRemoval):
    def remove(self, tokens):
        tokens_without_special_char = []
        for token in tokens:
            if str(''.join(filter(str.isalnum, token))) != '':
                tokens_without_special_char.append(''.join(filter(str.isalnum, token)))
        return tokens_without_special_char
