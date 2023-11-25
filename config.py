import os

from dotenv import load_dotenv

load_dotenv()

# Qdrant
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
COLLECTION_NAME = "products"

# OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
