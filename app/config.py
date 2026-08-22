import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
    QDRANT_URL = os.getenv("QDRANT_CLUSTER_ENDPOINT")
    QDRANT_COLLECTION = "Enterprise_RAG"

    GROQ_MODEL = "openai/gpt-oss-120b"
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    PORTKEY_API_KEY = os.getenv("PORTKEY_API_KEY")
    PORTKEY_CONFIG_SLUG =  os.getenv("PORTKEY_CONFIG_SLUG")
    GROQ_SLUG = "rag"
    GROQ_SLUG_2 = "rag2"



settings = Settings()



