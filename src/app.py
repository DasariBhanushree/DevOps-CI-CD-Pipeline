from flask import Flask
import socket
import os

@app.route("/")
def home():
    message = os.getenv("MESSAGE", "Default")
    password = os.getenv("PASSWORD", "NoPass")
    return f"{message} | Password: {password} | Pod: {socket.gethostname()}"

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
