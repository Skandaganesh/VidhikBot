from langchain_mongodb.vectorstores import MongoDBAtlasVectorSearch
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.schema import Document
from typing import List
from app.db.connect import db

embeddings = HuggingFaceEmbeddings()

async def create_vectorstore() -> MongoDBAtlasVectorSearch | None:
    try: 
        if db is None:
            raise Exception("DB is not connected")
        vector_store = MongoDBAtlasVectorSearch(
            collection = db["knowledge_base_chunks"],         
            embedding = embeddings,
            index_name = "vector_index" 
        )
        return vector_store
    except Exception as e:
        print(f"error in retreiver: {e}")
        return None
    
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