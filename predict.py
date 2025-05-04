import requests

data = {
    "engine_size": 2.0,
    "cylinders": 4,
    "fuel_type": "Z",
    "transmission": "AS5",
    "distance": 150
}

response = requests.post("http://localhost:5000/predict", json=data)

if response.status_code == 200:
    result = response.json()
    print("Konsumsi per 100 km:", result["consumption_per_100km"], "liter")
    print("Jarak Tempuh:", result["distance_km"], "km")
    print("Total BBM:", result["total_fuel_liters"], "liter")
else:
    print("Gagal menghubungi API")
