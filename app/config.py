import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
    QDRANT_URL = os.getenv("QDRANT_CLUSTER_ENDPOINT")
    QDRANT_COLLECTION = "Enterprise_RAG"

    GROQ_MODEL = "llama-3.3-70b-versatile"
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")


settings = Settings()



