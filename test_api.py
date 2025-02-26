from fastapi.testclient import TestClient
from app.main import *

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}

def test_summarization_api():
    response = client.post("/summarize", json={"text": "Patient with chest pain."})
    assert response.status_code == 200
    assert "summary" in response.json()