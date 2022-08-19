import contractions
import numpy

from lib.preprocessing.pheme.bert_embedding.bert_embedding import BertEmbedding
import torch
import logging
import matplotlib.pyplot as plt

from pytorch_pretrained_bert import BertTokenizer, BertModel, BertForMaskedLM


class BertEmbeddingImpl(BertEmbedding):
    def bert_embed(self, text):
        # todo
        # OPTIONAL: if you want to have more information on what's happening, activate the logger as follows
        logging.basicConfig(level=logging.INFO)

        # plt.inline

        # Load pre-trained model tokenizer (vocabulary)
        tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        text = "Here is the sentence I want embeddings for."
        marked_text = "[CLS] " + text + " [SEP]"

        # Tokenize our sentence with the BERT tokenizer.
        tokenized_text = tokenizer.tokenize(marked_text)

        # Print out the tokens.
        print(tokenized_text)
