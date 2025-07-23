from app.core.config import HF_TOKEN, REPO_ID
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace

def createLLM(): 
    try:
        llm = HuggingFaceEndpoint(
            repo_id=REPO_ID,
            task="conversational",
            max_new_tokens=512,
            do_sample=False,
            repetition_penalty=1.03,
            huggingfacehub_api_token=HF_TOKEN
        )
        
        chat_llm = ChatHuggingFace(llm=llm, verbose=True)
        print("LLM Initialized")
        return chat_llm
    except Exception as e:
        print(f"LLM Initialization failed {str(e)}")
        return None

chat_llm = createLLM()

def build_context(docs):
    return ""

def generate_answer(query: str, chat_history: list):
    return ""
