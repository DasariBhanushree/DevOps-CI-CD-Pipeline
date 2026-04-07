from flask import Flask
import socket
import os

app = Flask(__name__)

@app.route("/")
def home():
    message = os.getenv("MESSAGE", "Default Message")
    return f"{message} | Pod: {socket.gethostname()}"

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
