
# Weather Data Storage Service (Flask + Google Cloud Platform)

This is a Flask-based backend service that fetches historical weather data from the Open-Meteo API and stores it in Google Cloud Storage. The project is deployed using Google Cloud Run.

---

## Live Demo

**URL:** [https://weather-service-266316618620.us-central1.run.app](https://weather-service-266316618620.us-central1.run.app)

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/weather-data-service.git
cd weather-data-service
````

### 2. Create a virtual environment and install dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Set Environment Variables

```bash
export GCS_BUCKET_NAME=your-gcs-bucket-name
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/your-service-account-key.json
```

### 4. Run the Flask server locally

```bash
python app.py
```

---

## Deploy to Google Cloud Run

1. **Enable required services:**

```bash
gcloud services enable run cloudbuild.googleapis.com
```

2. **Deploy the service:**

```bash
gcloud run deploy weather-service \
  --source . \
  --region us-central1 \
  --platform managed \
  --allow-unauthenticated \
  --set-env-vars GCS_BUCKET_NAME=your-gcs-bucket-name
```

---

## Folder Structure
```
weather-backend-service/
│
├── main.py               # Flask app with all routes and Handles Open-Meteo API integration
├── Dockerfile            # Docker container definition
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation (this file)
```

## API Documentation

### 1. `/store-weather-data` — **POST**

* **Description:** Fetches weather data and stores it in Google Cloud Storage.
* **Endpoint:** `/store-weather-data`
* **Method:** `POST`
* **Request Body (JSON):**

```json
{
  "latitude": 13.08,
  "longitude": 80.27,
  "start_date": "2024-01-01",
  "end_date": "2024-01-07"
}
```

* **Success Response:**

```json
{
  "message": "Data stored successfully",
  "file_name": "weather_13_08_80_27_2024-01-01_to_2024-01-07.json"
}
```

* **Error Codes:**

  * `400`: Invalid or missing inputs
  * `502`: Open-Meteo API failure
  * `500`: Internal server error

---

### 2. `/list-weather-files` — **GET**

* **Description:** Lists all weather files stored in the bucket.
* **Endpoint:** `/list-weather-files`
* **Method:** `GET`
* **Response:**

```json
{
  "files": [
    "weather_13_08_80_27_2024-01-01_to_2024-01-07.json"
  ]
}
```

---

### 3. `/weather-file-content/<file_name>` — **GET**

* **Description:** Returns the content of a specific file.
* **Endpoint Example:** `/weather-file-content/weather_13_08_80_27_2024-01-01_to_2024-01-07.json`
* **Method:** `GET`
* **Success Response:** JSON weather data
* **Error Code:** `404` if file not found, `500` for other errors

---

### 4. `/` — **GET**

* **Description:** Health check endpoint
* **Response:** `Weather Data API is running.`

---

## Environment Variables

| Variable                         | Description                                       |
| -------------------------------- | ------------------------------------------------- |
| `weather-data-bucket-manideepmukhi`                | Name of the Google Cloud Storage bucket           |


## Author
```Manideep Mukhi```


---



**Manideep Mukhi**

