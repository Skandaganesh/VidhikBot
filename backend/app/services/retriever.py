# from langchain.vectorstores import FAISS
# from langchain.embeddings import HuggingFaceEmbeddings

# def initialize_retriever(documents):
#     """
#     Initializes the retriever using FAISS and HuggingFace embeddings.

#     Args:
#         documents (list): List of documents.

#     Returns:
#         retriever: Initialized retriever.
#     """
#     embeddings = HuggingFaceEmbeddings()
#     db = FAISS.from_documents(documents, embeddings)
#     return db.as_retriever(search_kwargs={"k": 3})
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

def load_retriever():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.load_local("vector_store", embeddings)
    return db.as_retriever(search_kwargs={"k": 3})


def initialize_retriever():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.load_local("vector_store", embeddings)
    return db.as_retriever(search_kwargs={"k": 3})
