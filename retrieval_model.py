import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# load dataset
documents = pd.read_csv('documents.csv')

# loade5 embedding model
model = SentenceTransformer("intfloat/e5-base-v2")


# load encoded documents
doc_emb = np.load('document_embeddings.npy')



# retrieval function

def retrieval(query, topk=5):
    #encode user's query
    query_emb = model.encode([query])

    # calculate cosine similarity
    scores = cosine_similarity(query_emb, doc_emb)[0]

    # get position of top docs
    top_indices = np.argsort(scores)[::-1][:topk]

    # retrieve the documents
    re_docs = documents[ ["document_id", "title", "text", "source"]].iloc[top_indices].copy()
 
    return re_docs
