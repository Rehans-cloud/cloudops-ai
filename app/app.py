from flask import Flask, jsonify, render_template
from datetime import datetime, timezone

app = Flask(__name__, template_folder="templates")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "CloudOps AI",
        "timestamp": datetime.now(timezone.utc).isoformat()
    })

@app.route("/api/status")
def status():
    return jsonify({
        "system": "CloudOps AI",
        "status": "running",
        "message": "Monitoring platform is operational"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)