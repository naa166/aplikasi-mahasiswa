import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "source-code"))
from app import app

def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"