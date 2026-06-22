from flask import Flask, jsonify
import os

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)