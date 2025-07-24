from app.core.config import PROVIDER_BASE_URL, PROVIDER_API_KEY, LLM_MODEL_NAME
from langchain_openai import ChatOpenAI

def createLLM(): 
    try:
        chat_llm = ChatOpenAI(
            base_url=PROVIDER_BASE_URL,
            api_key=PROVIDER_API_KEY,
            model=LLM_MODEL_NAME,
            temperature=0.7,
            max_tokens=None,
            max_completion_tokens=150,
            max_retries=2,
            verbose=True,
        )
        print("LLM Initialized")
        return chat_llm
    except Exception as e:
        print(f"LLM Initialization failed {str(e)}")
        return None

chat_llm = createLLM()