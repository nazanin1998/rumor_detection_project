from lib.preprocessing.pheme.bert_embedding.bert_embedding import BertEmbedding


class BertEmbeddingImpl2(BertEmbedding):
    def __init__(self):
        from sentence_transformers import SentenceTransformer
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def bert_embed(self, text):
        # todo => we must divide sentences but this sentences can not divide because we remove sign from paragraph.
        # Our sentences we like to encode
        sentences = [text]

        # Sentences are encoded by calling model.encode()
        embeddings = self.model.encode(sentences)
        return embeddings
        # # Print the embeddings
        # for sentence, embedding in zip(sentences, embeddings):
        #     print("Sentence:", sentence)
        #     print("Embedding:", embedding)
        #     print("")
