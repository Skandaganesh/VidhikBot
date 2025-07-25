from app.services.retriever import create_retriever
from app.utils.chatbot_utils import docs_to_str
from app.services.chatbot import rag_chatbot

async def generate_answer(user_query: str, chat_history: str):
    try:
        if rag_chatbot is None:
            raise Exception("No chatbot found")
        print("chatbot active.")
        retriever = await create_retriever()
        if retriever is None:
            raise Exception("No retriever found")
        print("retriever active.")
        print("retrieving context...")
        docs = await retriever.ainvoke(user_query)
        context = docs_to_str(docs)
        print("chatbot responding...")
        chat_response = await rag_chatbot.ainvoke({ "context": context, "query": user_query, "chat_history": chat_history })
        print(f"chatbot response: {len(chat_response)}")
        return chat_response
    except Exception as e:
        print(f"an error: {str(e)}")
        return ""