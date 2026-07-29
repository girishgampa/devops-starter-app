from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

# Simple in-memory counter — resets when the app restarts.
# Good enough for now; this is exactly the kind of thing
# Prometheus will scrape later in the project.
request_count = 0


@app.route("/")
def home():
    global request_count
    request_count += 1
    return jsonify({
        "message": "Hello, DevOps!",
        "hostname": socket.gethostname(),
        "request_count": request_count
    })


@app.route("/health")
def health():
    # Kubernetes will call this to check if the app is alive.
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
