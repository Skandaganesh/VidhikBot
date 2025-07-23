from langchain_mongodb.vectorstores import MongoDBAtlasVectorSearch
from langchain_huggingface import HuggingFaceEmbeddings
from app.db.connect import connectDB

db = connectDB()
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