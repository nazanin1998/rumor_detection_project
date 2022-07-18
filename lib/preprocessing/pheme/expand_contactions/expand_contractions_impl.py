import contractions

from lib.preprocessing.pheme.expand_contactions.expand_contractions import ExpandContractions


class ExpandContractionsImpl(ExpandContractions):
    def expand(self, text):
        print('expand contraction impl1')
        expanded_words = []
        for word in text.split():
            try:
                expanded_words.append(contractions.fix(word))
            except:
                print("baby", end=' ')
                print(word, end=' ')
                break

        return ' '.join(expanded_words)
