from lib.preprocessing.pheme.bert_embedding.bert_embedding import BertEmbedding


class BertEmbeddingImpl2(BertEmbedding):
    def bert_embed(self, text):
        from sentence_transformers import SentenceTransformer
        model = SentenceTransformer('all-MiniLM-L6-v2')

        # todo => we must divide sentences but this sentences can not divide because we remove sign from paragraph.
        # Our sentences we like to encode
        sentences = [text]

        # Sentences are encoded by calling model.encode()
        embeddings = model.encode(sentences)

        # Print the embeddings
        for sentence, embedding in zip(sentences, embeddings):
            print("Sentence:", sentence)
            print("Embedding:", embedding)
            print("")
