# Historical Weather Data Backend Service

This backend service fetches historical weather data from the [Open-Meteo Historical Weather API](https://open-meteo.com/en/docs/historical-weather-api), stores the data as JSON files (simulating cloud storage), and provides endpoints to list and retrieve those files.

 **Note**: Deployment to Google Cloud Run was skipped due to budget constraints. However, the application is fully functional and has been tested locally using Docker and Postman.

---

## Tech Stack

- **Backend Framework**: Python + Flask  
- **Cloud Integration**: Simulated using local file storage (no billing needed)  
- **Containerization**: Docker  
- **Testing Tool**: Postman  

---

##  Features

- Fetches historical weather data using Open-Meteo API
- Stores data as JSON files with a structured naming convention
- Lists stored JSON files
- Retrieves the content of a specific stored file

---

## API Endpoints

### 1. `POST /store-weather-data`

**Purpose**: Fetch weather data and store it as a JSON file

- **Method**: `POST`
- **URL**: `http://localhost:5000/store-weather-data`
- **Request Body**:
```json
{
  "latitude": 52.54833,
  "longitude": 13.407822,
  "start_date": "2023-05-01",
  "end_date": "2023-05-02"
}


Response:

json
Copy
Edit
{
  "message": "Weather data stored successfully",
  "file_name": "weather_52.54833_13.407822_2023-05-01_2023-05-02.json"
}
2. GET /list-weather-files
Purpose: List all JSON files stored in the weather_data/ directory.

Method: GET

URL: http://localhost:5000/list-weather-files

Response:

json
Copy
Edit
{
  "files": [
    "weather_52.54833_13.407822_2023-05-01_2023-05-02.json",
    "weather_40.7128_74.006_2022-01-01_2022-01-03.json"
  ]
}
3. GET /weather-file-content/<file_name>
Purpose: Retrieve the contents of a specific weather JSON file.

Method: GET

URL: http://localhost:5000/weather-file-content/weather_52.54833_13.407822_2023-05-01_2023-05-02.json

Response:

json
Copy
Edit
{
  "latitude": 52.54833,
  "longitude": 13.407822,
  "daily": {
    "temperature_2m_max": [...],
    "temperature_2m_min": [...],
    ...
  }
 Run Locally with Docker
 Prerequisites
Docker installed
 Build Docker Image
bash
Copy
Edit
docker build -t weather-service .
 Run the App
bash
Copy
Edit
docker run -p 5000:5000 weather-service
The app will now be available at:
 http://localhost:5000

 File Storage
All weather JSON files are stored in the weather_data/ directory inside your project root. This simulates Google Cloud Storage.

 Testing the API
You can use Postman or curl to test the endpoints locally.

Example with curl:

bash
Copy
Edit
curl -X POST http://localhost:5000/store-weather-data \
-H "Content-Type: application/json" \
-d '{"latitude":52.54833,"longitude":13.407822,"start_date":"2023-05-01","end_date":"2023-05-02"}'
 Notes
Make sure the weather_data/ directory exists before running.

The Open-Meteo API is free and does not require an API key.

Full error handling is implemented for invalid inputs and file not found errors.

 Author
Manideep Mukhi
(Java Backend Developer | Spring Boot | Python Enthusiast | Cloud Explorer)


