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

def test_redirect():
    payload = {
        "original_url": "https://example.com/"
    }
    create_response = client.post("/url/", json = payload)
    assert create_response.status_code == 200
    response_data = create_response.json()
    short_url = response_data["short_code"]
    redirect_response = client.get(f"/{short_url}", follow_redirects=False)
    assert redirect_response.status_code in (302, 307)
    assert redirect_response.headers["location"] == payload["original_url"]