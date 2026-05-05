from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_chat():
    response = client.post("/chat", data={"message": "What is Docker?"})
    assert response.status_code == 200
    assert "Docker" in response.json()["reply"] or "docker" in response.json()["reply"].lower()