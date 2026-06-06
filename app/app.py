from flask import Flask, jsonify
import socket
import os

app = Flask(__name__)

VERSION = os.environ.get("APP_VERSION", "v1")
COLOR = os.environ.get("APP_COLOR", "blue")

@app.route("/")
def home():
    return jsonify({
        "application": "k8s-platform-engineering",
        "version": VERSION,
        "color": COLOR,
        "pod": socket.gethostname()
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })

@app.route("/version")
def version():
    return jsonify({
        "version": VERSION,
        "color": COLOR
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
