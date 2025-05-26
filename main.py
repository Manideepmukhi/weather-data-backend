from flask import Flask, request, jsonify
import requests
import json
import os
from google.cloud import storage

app = Flask(__name__)


BUCKET_NAME = os.environ.get("GCS_BUCKET_NAME")

@app.route("/store-weather-data", methods=["POST"])
def store_weather_data():
    data = request.get_json()
    latitude = data.get("latitude")
    longitude = data.get("longitude")
    start_date = data.get("start_date")
    end_date = data.get("end_date")

    if not all([latitude, longitude, start_date, end_date]):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        url = (
            "https://archive-api.open-meteo.com/v1/archive?"
            f"latitude={latitude}&longitude={longitude}"
            f"&start_date={start_date}&end_date={end_date}"
            "&daily=temperature_2m_max,temperature_2m_min,temperature_2m_mean,"
            "apparent_temperature_max,apparent_temperature_min,apparent_temperature_mean"
            "&timezone=auto"
        )

        response = requests.get(url)
        weather_data = response.json()

        if "daily" not in weather_data:
            return jsonify({"error": "Failed to fetch weather data"}), 500

        file_name = f"weather_{latitude}_{longitude}_{start_date}_to_{end_date}.json"

        client = storage.Client()
        bucket = client.bucket(BUCKET_NAME)
        blob = bucket.blob(file_name)
        blob.upload_from_string(json.dumps(weather_data), content_type="application/json")

        return jsonify({"message": "Data stored successfully", "file_name": file_name}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/list-weather-files", methods=["GET"])
def list_weather_files():
    try:
        client = storage.Client()
        bucket = client.bucket(BUCKET_NAME)
        blobs = bucket.list_blobs()
        files = [blob.name for blob in blobs]
        return jsonify({"files": files}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/weather-file-content/<file_name>", methods=["GET"])
def get_weather_file(file_name):
    try:
        client = storage.Client()
        bucket = client.bucket(BUCKET_NAME)
        blob = bucket.blob(file_name)
        if not blob.exists():
            return jsonify({"error": "File not found"}), 404
        content = blob.download_as_string()
        return jsonify(json.loads(content)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/", methods=["GET"])
def index():
    return "Weather Data API is running."
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)