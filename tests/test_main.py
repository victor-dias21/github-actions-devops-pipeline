from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_root_returns_service_status() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "service": "github-actions-devops-pipeline",
        "status": "ok",
    }


def test_healthcheck_returns_healthy() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
