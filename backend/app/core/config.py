import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
REPO_ID = os.getenv("REPO_ID")

# HuggingFace configuration
os.environ["HUGGINGFACEHUB_API_TOKEN"] = HF_TOKEN
