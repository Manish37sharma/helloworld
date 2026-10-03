from hello import app


def test_home_page():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"Hello World" in response.data


def test_api_hello():
    client = app.test_client()

    response = client.get("/api/hello")

    assert response.status_code == 200
    assert response.json["status"] == "success"
    assert response.json["message"] == "Hello from my first REST API"