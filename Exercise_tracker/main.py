import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# nutritionix env
NUTRITIONIX_ID = os.getenv("NUTRITIONIX_ID")
NUTRITIONIX_API_KEY = os.getenv("NUTRITIONIX_API_KEY")
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

# Sheety env
SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")
SHEETY_ENDPOINT = (
    "https://api.sheety.co/0cb5b5e2e15bc0dbbbc6ed109bf60073/workoutTracking/workouts"
)


# Get exercise data (Nutritionix API)
WEIGHT = 87
HEIGHT = 187
AGE = 26
user_query = input("Tell me which exercise you did and for how long?: ")

nutritionix_header = {
    "x-app-id": NUTRITIONIX_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}

nutritionix_params = {
    "query": user_query,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}

nutritionix_response = requests.post(
    url=NUTRITIONIX_ENDPOINT,
    json=nutritionix_params,
    headers=nutritionix_header,
)

result = nutritionix_response.json()

# Record data in a Google sheet. (Sheety API)
sheety_auth = {
    "Authorization": SHEETY_TOKEN,
}

today = datetime.now().strftime("%d/%M/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    data_row = {
        "workout": {
            "date": today,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheety_response = requests.post(
        url=SHEETY_ENDPOINT, json=data_row, headers=sheety_auth
    )

    print(sheety_response.text)
