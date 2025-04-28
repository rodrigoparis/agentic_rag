import os
import sys
from huggingface_hub import login
from dotenv import load_dotenv
from utils.logger import logger
from utils.config import Config

def authenticate():
    try:
        if not Config.HUGGINGFACEHUB_API_TOKEN:
            raise ValueError("Missing HUGGINGFACEHUB_API_TOKEN in .env file. Exiting...")
        else:
            login(token=Config.HUGGINGFACEHUB_API_TOKEN)
            logger.info("✅ Authentication successful")
    except Exception as e:
        logger.error(f"❌ Auth error: {e}")
        sys.exit(1)
