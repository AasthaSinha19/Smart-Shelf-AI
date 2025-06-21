# ---- app.py ----
from flask import Flask, jsonify
from flask_cors import CORS
from dummy_data import get_dummy_alerts, get_dummy_trending

app = Flask(__name__)
CORS(app)

@app.route("/")
def html_home():
    return "<h1 style='text-align:center; text-decoration: underline; color:#003366;'>Smart Shelf API is live!</h1>"

@app.route("/api/status")
def api_home():
    return jsonify({"message": "Smart Shelf API is live!"})

@app.route("/alerts")
def alerts():
    alerts_data = get_dummy_alerts()
    return jsonify(alerts_data)

@app.route("/trending")
def trending():
    trending_data = get_dummy_trending()
    return jsonify(trending_data)

if __name__ == "__main__":
    app.run(debug=True)
