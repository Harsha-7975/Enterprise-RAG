import logfire
from qdrant_client import QdrantClient
from qdrant_client.http import models
from app.config import settings
from app.services.retrieval.embeddings import embed_query


#initialize qdrant client
client = QdrantClient(
    url = settings.QDRANT_URL,
    api_key=settings.QDRANT_API_KEY
)

def search_enterprise_knowledge(query: str,limit: int=8):
    """
    Performs a high-precision search in the enterprise knowledge base.
    """
    try:
        query_vector = embed_query(query)

        response = client.query_points(
            collection_name=settings.QDRANT_COLLECTION,
            query = query_vector,
            limit = limit,
            with_payload=True
        )

        results = []
        for res in response.points:
            results.append({
                "content" : res.payload.get("text",""),
                "source": res.payload.get("source","Unknown"),
                "score":res.score
            })
        return results
    except Exception as e:
        logfire.error(f"Qdrant Serach Failed: {e}")
        return []

if __name__=="__main__":
    query = "What is kubernetes?"
    print(search_enterprise_knowledge(query))