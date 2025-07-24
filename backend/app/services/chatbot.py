from app.services.prompts import chat_prompt
from app.services.llm import chat_llm
from langchain_core.output_parsers import StrOutputParser

def create_rag_chatbot():
    try:
        parser = StrOutputParser()
        chain =  chat_prompt | chat_llm | parser
        print("RAG Chatbot initialized")
        return chain
    except Exception as e:
        print(f"an error in RAG chatbot: {str(e)}")
        return None
    
rag_chatbot = create_rag_chatbot()