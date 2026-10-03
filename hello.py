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

    return jsonify({
        "message": "User created successfully",
        "user": data
    }), 201


if __name__ == "__main__":
    app.run(debug=True)