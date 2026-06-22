from flask import Flask, jsonify
import os
from datetime import datetime

app = Flask(__name__)

counter = 0

@app.route("/")
def home():
    return jsonify({
        "message": "Hello from my CI/CD Pipeline!",
        "status": "running",
        "version": "1.0.0"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/about")
def about():
    return jsonify({
        "project": "Flask CI/CD Pipeline",
        "author": "preethar10",
        "tech": ["Python", "Flask", "GitHub Actions"]
    })

@app.route("/counter")
def visit_counter():
    global counter
    counter += 1
    return jsonify({
        "visits": counter,
        "message": f"This API has been visited {counter} time(s)!"
    })

@app.route("/time")
def current_time():
    now = datetime.now()
    return jsonify({
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%H:%M:%S"),
        "message": f"Current date and time is {now.strftime('%Y-%m-%d %H:%M:%S')}"
    })

if __name__ == "__main__":
    app.run(debug=True)