from fastapi import FastAPI, Query
from weaviate_client import client
from weaviate.classes.query import MetadataQuery
from dotenv import load_dotenv




app = FastAPI()

@app.post("/search")
def search_diseases(q: str = Query(..., description="Search query")):
    try:
        result = client.collections.get("Agri_gpt_vdb").query.hybrid(
            query=q,
            return_properties=["disease_id", "disease_name"],
            alpha=0.8,
            return_metadata=MetadataQuery(score=True, explain_score=True),
            limit=7,
        )

        sorted_data = sorted(result.objects, key=lambda o: o.metadata.score, reverse=True)

        return [
            {
                "disease_id": obj.properties["disease_id"],
                "disease_name": obj.properties["disease_name"],
                "score": obj.metadata.score
            }
            for obj in sorted_data
        ]

    except Exception as e:
        return {"error": str(e)}
