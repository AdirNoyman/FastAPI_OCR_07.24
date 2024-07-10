from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_post_home():
    response = client.post("/")
    assert response.status_code == 200
    assert "application/json" in response.headers["Content-Type"]
    assert response.json() == {"Hello": "Adiros details"}
