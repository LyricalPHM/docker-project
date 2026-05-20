from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
import time

app = Flask(__name__)

REQUESTS = Counter(
    "flask_app_requests_total",
    "Total number of requests to the Flask application"
)

@app.route("/")
def home():
    REQUESTS.inc()
    return "Hello, Continuous Deployment from VPS!"

@app.route("/health")
def health():
    REQUESTS.inc()
    return "OK"

@app.route("/cpu")
def cpu_load():
    REQUESTS.inc()
    end = time.time() + 0.3
    x = 0
    while time.time() < end:
        x += 1
    return f"CPU load generated: {x}"

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
