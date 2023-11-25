from chromadb import Settings, HttpClient
from chromadb.utils import embedding_functions

from config import (
    COLLECTION_NAME,
    DB_HOST,
    DB_PORT,
)

chroma_client = HttpClient(host=DB_HOST, port=DB_PORT, settings=Settings(allow_reset=True, anonymized_telemetry=False))
sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
chroma_collection = chroma_client.get_or_create_collection(COLLECTION_NAME, embedding_function=sentence_transformer_ef)
