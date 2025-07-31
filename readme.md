# Agri Disease Search API

A FastAPI backend service that connects to a Weaviate Cloud vector database to perform hybrid semantic search on disease information for agriculture.  
The API exposes a `/search` endpoint which the Android app can call to get relevant disease data.

---

## Features

- Connects securely to Weaviate Cloud with API keys  
- Uses OpenAI embeddings for semantic search via Weaviate’s `text2vec-openai` module  
- Returns top disease results sorted by relevance score  
- Simple REST GET endpoint: `/search?q=your_query`  

---

## Prerequisites

- Python 3.9+  
- Weaviate Cloud instance with `text2vec-openai` module enabled  
- OpenAI API key  
- Weaviate API key with proper roles  
- AWS (or any Linux server) for deployment  

---

## Setup & Deployment

### 1. Clone the repo

bash
git clone https://github.com/your-org/agri-disease-search-api.git
cd agri-disease-search-api

### 2. .env
.env should have
OPENAI_APIKEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx
WEAVIATE_URL=https://your-weaviate-cloud-instance.weaviate.network
WEAVIATE_API_KEY=your-weaviate-api-key

### 3.Install dependencies
pip install -r requirements.txt

### 4. Run locally (for testing)
uvicorn main:app --reload

###### 5.Test your API by opening in browser:
http://localhost:8000/search?q=রোগ