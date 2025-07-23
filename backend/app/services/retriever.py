from langchain_core.vectorstores import VectorStoreRetriever
from langchain.schema import Document
from typing import List
from app.services.vector_store import create_vectorstore

async def store_in_vectorstore(documents: List[Document]) -> bool:
    try: 
        vector_store = await create_vectorstore()
        if vector_store is None:
            raise Exception("Vectorstore not available")
        doc_ids = await vector_store.aadd_documents(documents=documents)
        print(f"{len(doc_ids)} Documents stored")
        return True
    except Exception as e:
        print(f"error in retreiver: {e}")
        return False

async def create_retriever() -> VectorStoreRetriever | None:
    try:
        default_search_kwargs = {
            'k': 3,
            'score_threshold': 0.6
        }
        vector_store = await create_vectorstore()
        if vector_store is None:
            raise Exception("Vectorstore not available")
        retriever = vector_store.as_retriever(search_kwargs=default_search_kwargs)
        return retriever
    except Exception as e:
        print(f"error in retreiver: {e}")
        return None
