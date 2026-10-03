from flask import Flask, jsonify

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


if __name__ == "__main__":
    app.run(debug=True)