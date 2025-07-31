<<<<<<< HEAD
import os
import weaviate
from dotenv import load_dotenv

load_dotenv()
OPENAI_APIKEY = os.getenv("OPENAI_APIKEY")
WEAVIATE_URL = os.getenv("WEAVIATE_URL")
WEAVIATE_API_KEY = os.getenv("WEAVIATE_API_KEY")

client = weaviate.connect_to_weaviate_cloud(
    cluster_url=WEAVIATE_URL,
    auth_credentials=weaviate.auth.AuthApiKey(WEAVIATE_API_KEY),
    headers={
        "X-OpenAI-Api-Key": OPENAI_APIKEY  # Replace with your inference API key
    }
)
=======
import os
import weaviate
from dotenv import load_dotenv

load_dotenv()
OPENAI_APIKEY = os.getenv("OPENAI_APIKEY")
WEAVIATE_URL = os.getenv("WEAVIATE_URL")
WEAVIATE_API_KEY = os.getenv("WEAVIATE_API_KEY")

client = weaviate.connect_to_weaviate_cloud(
    cluster_url=WEAVIATE_URL,
    auth_credentials=weaviate.auth.AuthApiKey(WEAVIATE_API_KEY),
    headers={
        "X-OpenAI-Api-Key": OPENAI_APIKEY  # Replace with your inference API key
    }
)
>>>>>>> dd1fad9b86a05d2984b5760d8b8f0fd01e34a043
