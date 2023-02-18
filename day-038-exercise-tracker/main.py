from dotenv import load_dotenv
import os
import requests
from datetime import datetime

"""
Calories tracker using natural language input. Entries added to a google sheet.

The google sheet used:
https://docs.google.com/spreadsheets/d/10A97iRjWFQV5xVDUgTlwwW7vfaMLs67xXq-yfLOlmg4/
"""

# .env
load_dotenv(".env")
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
SHEETY_AUTH_TOKEN = os.getenv("SHEETY_AUTH_TOKEN")
weight = float(os.getenv("WEIGHT"))
height = float(os.getenv("HEIGHT"))
age = int(os.getenv("AGE"))

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
nutrix_query = input("What exercises did you do?: ")
nutrix_header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

nutrix_params = {
    "query": nutrix_query,
    "gender": "male",
    "weight_kg": weight,
    "height_cm": height,
    "age": age,
}

# Send request for exercise data
response = requests.post(
    url=exercise_endpoint, json=nutrix_params, headers=nutrix_header
)
exercises_data = response.json()["exercises"]

# For formatting rows to be added to google sheet.
exercises = []
now_date = datetime.now().strftime(r"%d/%m/%Y")
now_time = datetime.now().strftime("%X")
for exercise in exercises_data:
    activity = exercise["user_input"]
    cal_burned = exercise["nf_calories"]
    duration = exercise["duration_min"]
    data = {
        "date": now_date,
        "time": now_time,
        "exercise": activity.capitalize(),
        "duration": duration,
        "calories": cal_burned,
    }
    exercises.append(data)

# Request for appending rows to google sheet.
sheety_bearer = {
    "Authorization": f"Bearer {SHEETY_AUTH_TOKEN}",
}
sheety_endpoint = (
    "https://api.sheety.co/c0aa8f07268eebeeb7c237f161de056d/myWorkouts/workouts"
)


for data in exercises:
    row = {"workout": data}
    r = requests.post(url=sheety_endpoint, json=row, headers=sheety_bearer)
print(f"Logged {len(exercises)} entries.")
