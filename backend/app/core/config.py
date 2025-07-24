import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()
 
HF_TOKEN = os.getenv("HF_TOKEN")
REPO_ID = os.getenv("REPO_ID")
DATABASE_URL = os.getenv("DATABASE_URL")
PROVIDER_BASE_URL= os.getenv("PROVIDER_BASE_URL")
PROVIDER_API_KEY= os.getenv("PROVIDER_API_KEY")
LLM_MODEL_NAME= os.getenv("LLM_MODEL_NAME")

# HuggingFace configuration
os.environ["HUGGINGFACEHUB_API_TOKEN"] = HF_TOKEN
