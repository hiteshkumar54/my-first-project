from flask import Flask, jsonify

# Create Flask app
app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return "Autonomous Cloud Cost Intelligence Backend Running"

# Cost prediction route
@app.route("/cost")
def get_cost():
    data = {
        "current_cost": 720,
        "predicted_cost": 850,
        "recommendation": "Stop unused instances to reduce cost by ₹130"
    }
    return jsonify(data)

# Run server
if __name__ == "__main__":
    app.run(debug=True)
