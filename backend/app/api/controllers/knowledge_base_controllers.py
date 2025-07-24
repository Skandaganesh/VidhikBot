from fastapi.responses import JSONResponse
from app.services.doc_loaders import create_documents
from app.services.vector_store import store_in_vectorstore
from app.services.retriever import create_retriever
from app.api.models import KnowlegdeQuery

async def create_knowledge_base() -> JSONResponse:
    try:
        documents = await create_documents()
        if documents is None:
            raise Exception("No documents created")
        print('Document chunks are created')
        is_stored = await store_in_vectorstore(documents)
        if is_stored == False:
            raise Exception("Document chunks were not stored in vectorstore")
        print('Documents stored in vectorstore')
        return JSONResponse(status_code=201, content={ "data": f"{len(documents)} document chunks created and stored in vectorstore", "message":"document chunks created and stored in vectorstore"})
    except Exception as e:
        print(f"Error in creating knowledge base: {str(e)}")
        raise JSONResponse(status_code=500, content={ "data":None, "message":"Error in creating knowledge base"})
    
async def check_knowledge_base(query: KnowlegdeQuery) -> JSONResponse:
    try:
        retriever = await create_retriever()
        if retriever is None:
            raise Exception("Retreiver not found")
        docs = retriever.invoke(query.user_query)
        print('Documents retrieved')
        return JSONResponse(status_code=200, content={ "data": { "documents": [doc.model_dump() for doc in docs] }, "message":"Documents retrieved"})
    except Exception as e:
        print(f"Error in checking knowledge base: {str(e)}")
        raise JSONResponse(status_code=500, content={ "data":None, "message":"Error in documents retrieving"})