import contractions
import numpy

from lib.preprocessing.pheme.expand_contactions.expand_contractions import ExpandContractions


class ExpandContractionsImpl(ExpandContractions):
    def expand(self, text):
        expanded_words = []
        if text is numpy.NaN or text is None:
            return None
        for word in text.split():
            try:
                expanded_words.append(contractions.fix(word))
            except:
                break
        text = ' '.join(expanded_words)
        return text
