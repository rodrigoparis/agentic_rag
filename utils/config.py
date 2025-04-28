import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    KNOWLEDGE_FILE_PATH = os.getenv("KNOWLEDGE_FILE_PATH", "INdata/text.pdf")
    HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
