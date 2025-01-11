from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

def initialize_retriever(documents):
    """
    Initializes the retriever using FAISS and HuggingFace embeddings.

    Args:
        documents (list): List of documents.

    Returns:
        retriever: Initialized retriever.
    """
    embeddings = HuggingFaceEmbeddings()
    db = FAISS.from_documents(documents, embeddings)
    return db.as_retriever(search_kwargs={"k": 3})
