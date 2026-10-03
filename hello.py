from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

DATABASE = "users.db"


def get_db_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def create_table():
    connection = get_db_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            role TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


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

    connection = get_db_connection()

    cursor = connection.execute(
        """
        INSERT INTO users (name, email, role)
        VALUES (?, ?, ?)
        """,
        (name, email, role)
    )

    connection.commit()

    user_id = cursor.lastrowid

    connection.close()

    return jsonify({
        "message": "User created successfully",
        "user_id": user_id
    }), 201


create_table()


if __name__ == "__main__":
    app.run(debug=True)