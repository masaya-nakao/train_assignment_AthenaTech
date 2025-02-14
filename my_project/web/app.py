from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@db:5432/mydb")

def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn

@app.route("/")
def hello():
    return "Hello, Docker!"

@app.route("/data")
def get_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM test") 
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rows)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)