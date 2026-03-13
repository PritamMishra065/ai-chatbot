import os
import faiss
import numpy as np

from models.embeddings import get_embedding_model



embedding_model = get_embedding_model()

documents = []
index = None


def load_documents(folder="data"):

    global documents
    documents = []

    for file in os.listdir(folder):

        path = os.path.join(folder, file)

        if file.endswith(".txt"):
            with open(path, "r", encoding="utf-8") as f:
                documents.append(f.read())


def build_index():

    global index

    if len(documents) == 0:
        return

    embeddings = embedding_model.encode(documents)

    embeddings = np.array(embeddings)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)


def retrieve_docs(query, k=3):


    if index is None:
        return []

    query_embedding = embedding_model.encode([query])

    distances, indices = index.search(np.array(query_embedding), k)

    results = []

    for i in indices[0]:
        if i < len(documents):
            results.append(documents[i])

    return results