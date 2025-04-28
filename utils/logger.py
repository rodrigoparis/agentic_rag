import os
import logging
from colorlog import ColoredFormatter
from dotenv import load_dotenv

load_dotenv()

os.makedirs("logs", exist_ok=True)

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()

logger = logging.getLogger("agentic_rag")
logger.setLevel(getattr(logging, LOG_LEVEL, logging.INFO))
logger.propagate = False

color_formatter = ColoredFormatter(
    "%(log_color)s%(asctime)s [%(levelname)s]%(reset)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    log_colors={
        'DEBUG':    'cyan',
        'INFO':     'green',
        'WARNING':  'yellow',
        'ERROR':    'red',
        'CRITICAL': 'bold_red',
    }
)

formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

# 📁 Archivo log
file_handler = logging.FileHandler("logs/app.log", encoding="utf-8")
file_handler.setFormatter(formatter)

# 🖥️ Consola
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

if not logger.hasHandlers():
    logger.addHandler(file_handler)
    logger.addHandler(file_handler)
