from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello World! My Internship Journey Has Started."


@app.route("/api/hello", methods=["GET"])
def api_hello():
    return jsonify({
        "message": "Hello from my first REST API",
        "status": "success"
    })


@app.route("/api/user", methods=["POST"])
def create_user():
    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Request body must contain JSON data"
        }), 400

    name = data.get("name")
    email = data.get("email")
    role = data.get("role")

    if not name:
        return jsonify({"error": "Name is required"}), 400

    if not email:
        return jsonify({"error": "Email is required"}), 400

    if not role:
        return jsonify({"error": "Role is required"}), 400

    return jsonify({
        "message": "User created successfully",
        "user": {
            "name": name,
            "email": email,
            "role": role
        }
    }), 201


if __name__ == "__main__":
    app.run(debug=True)