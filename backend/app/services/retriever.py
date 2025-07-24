from langchain_core.vectorstores import VectorStoreRetriever
from app.services.vector_store import create_vectorstore
from typing import Optional

async def create_retriever() -> Optional[VectorStoreRetriever]:
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
