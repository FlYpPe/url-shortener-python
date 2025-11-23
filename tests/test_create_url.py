from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_short_url(client):
    payload = {
        "original_url": "https://example.com"
    }

    response = client.post("/url/", json=payload)

    assert response.status_code == 200
    data = response.json()

    assert "short_code" in data
    assert data["original_url"] == "https://example.com/"