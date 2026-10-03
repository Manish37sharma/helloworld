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

def test_create_user():
    client = app.test_client()

    response = client.post(
        "/api/user",
        json={
            "name": "Manish Sharma",
            "email": "manish@example.com",
            "role": "Software Developer Intern"
        }
    )

    assert response.status_code == 201
    assert response.json["message"] == "User created successfully"
    assert response.json["user"]["name"] == "Manish Sharma"
    
def test_create_user_without_name():
    client = app.test_client()

    response = client.post(
        "/api/user",
        json={
            "email": "manish@example.com",
            "role": "Software Developer Intern"
        }
    )

    assert response.status_code == 400
    assert response.json["error"] == "Name is required"
    
def test_create_user_without_email():
    client = app.test_client()

    response = client.post(
        "/api/user",
        json={
            "name": "Manish Sharma",
            "role": "Software Developer Intern"
        }
    )

    assert response.status_code == 400
    assert response.json["error"] == "Email is required"