from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)

model = joblib.load("backend/hotchoco_model.pkl")
scale = joblib.load("backend/hotchoco_scaler.pkl")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    temperature = data["temperature"]
    humidity = data["humidity"]
    wind_speed = data["wind_speed"]
    is_weekend = data["is_weekend"]

    input_data = np.array([
        [temperature, humidity, wind_speed, is_weekend]
    ])

    scaled_data = scale.transform(input_data)

    prediction = model.predict(scaled_data)

    # Sales cannot be negative
    prediction = max(0, float(prediction[0]))

    return jsonify({
        "prediction": prediction
    })


if __name__ == "__main__":
    app.run(debug=True)