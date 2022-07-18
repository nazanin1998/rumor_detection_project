import contractions
import numpy

from lib.preprocessing.pheme.expand_contactions.expand_contractions import ExpandContractions


class ExpandContractionsImpl(ExpandContractions):
    def expand(self, text):
        print(text)
        expanded_words = []
        if text is numpy.NaN:
            return None
        for word in text.split():
            try:
                expanded_words.append(contractions.fix(word))
            except:
                print("baby", end=' ')
                print(word, end=' ')
                break
        text = ' '.join(expanded_words)
        return text
