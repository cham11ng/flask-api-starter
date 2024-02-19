"""Flask API tests."""

from src.app import app


def test_home():
    """Test home route."""
    with app.test_client() as client:
        res = client.get("/")
        json_data = res.get_json()

        assert json_data == {"name": "Flask API", "version": "0.1.0"}


def test_health_get():
    """Test health check with GET method."""
    with app.test_client() as client:
        res = client.get("/health?name=flask-api")
        json_data = res.get_json()

        assert json_data == {"data": {"name": "flask-api"}, "method": "GET"}
        assert res.status_code == 200


def test_health_post():
    """Test health check with POST method."""
    with app.test_client() as client:
        res = client.post(
            "/health",
            json={"name": "flask-api"},
            headers={"Content-Type": "application/json"},
        )
        json_data = res.get_json()

        assert json_data == {"data": {"name": "flask-api"}, "method": "POST"}
        assert res.status_code == 200


def test_health_delete():
    """Test health check with DELETE method should throw error."""
    with app.test_client() as client:
        res = client.delete("/health")
        json_data = res.get_json()

        assert json_data == {
            "code": "FC405",
            "message": "Method Not Allowed.",
        }
        assert res.status_code == 405


def test_dynamic():
    """Test dynamic route."""
    with app.test_client() as client:
        res = client.get("/dynamic/lorem-ipsum")
        json_data = res.get_json()

        assert json_data == {"url": "lorem-ipsum"}


def test_not_found():
    """Test not found."""
    with app.test_client() as client:
        res = client.get("/lorem-ipsum")
        json_data = res.get_json()

        assert json_data == {
            "code": "FC404",
            "message": "Not Found.",
        }
        assert res.status_code == 404


def test_server_error():
    """Test server error."""
    with app.test_client() as client:
        res = client.get("/error")
        json_data = res.get_json()

        assert json_data == {
            "code": "FC500",
            "message": "Internal Server Error.",
        }
        assert res.status_code == 500
