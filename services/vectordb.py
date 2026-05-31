import chromadb

from services.embeddings import create_embedding


client = chromadb.PersistentClient(
    path="chroma_db"
)


def get_collection():

    collection = client.get_or_create_collection(
        name="financial_documents"
    )

    return collection


def add_chunks(chunks):

    collection = get_collection()

    for i, chunk in enumerate(chunks):

        embedding = create_embedding(
            chunk
        )

        collection.add(
            ids=[str(i)],
            documents=[chunk],
            embeddings=[embedding.tolist()]
        )

def search_chunks(question, n_results=10):

    collection = get_collection()

    embedding = create_embedding(
        question
    )

    results = collection.query(
        query_embeddings=[
            embedding.tolist()
        ],
        n_results=n_results
    )

    return results