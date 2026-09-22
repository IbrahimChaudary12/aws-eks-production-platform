from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
import socket

app = Flask(__name__)

REQUESTS = Counter(
    "app_http_requests_total",
    "Total HTTP requests",
    ["endpoint"]
)

@app.route("/")
def home():
    REQUESTS.labels(endpoint="/").inc()
    return {
        "message": "AWS EKS Production Platform",
        "status": "running",
        "hostname": socket.gethostname()
    }

@app.route("/health")
def health():
    REQUESTS.labels(endpoint="/health").inc()
    return {"status": "healthy"}, 200

@app.route("/ready")
def ready():
    REQUESTS.labels(endpoint="/ready").inc()
    return {"status": "ready"}, 200

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
