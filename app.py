from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)


# Function to read Docker secrets
def get_secret(secret_name):
    try:
        with open(f"/run/secrets/{secret_name}", "r") as secret_file:
            return secret_file.read().strip()
    except:
        # Fallback for development
        return os.environ.get(secret_name, "default_value")


# Database setup with path from secrets
DB_PATH = "/app/data/notes.db"


def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    conn.execute(
        """
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT NOT NULL
    )
    """
    )
    conn.commit()
    conn.close()


@app.route("/")
def home():
    conn = get_db_connection()
    notes = conn.execute("SELECT * FROM notes").fetchall()
    conn.close()
    return render_template("index.html", notes=notes, db_user=get_secret("db_user"))


@app.route("/add", methods=["POST"])
def add_note():
    content = request.form["content"]
    if content.strip():
        conn = get_db_connection()
        conn.execute("INSERT INTO notes (content) VALUES (?)", (content,))
        conn.commit()
        conn.close()
    return redirect(url_for("home"))


if __name__ == "__main__":
    # Create data directory
    os.makedirs("/app/data", exist_ok=True)

    # Initialize database
    init_db()

    # Run Flask app
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
