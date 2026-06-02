import requests
from datetime import datetime
import os

X_APP_ID = os.environ.get("X_APP_ID")
X_APP_KEY = os.environ.get("X_APP_KEY")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
NUTRITION_ENDPOINT = os.environ.get("NUTRITION_ENDPOINT")
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
WEIGHT_KG = 58 # weight in Kg
HEIGHT_CM = 175 # height in centimeter
AGE = 18
GENDER = "male"
today = datetime.now()

NUTRITION_HEADER = {
    "Content-Type" : "application/json",
    "x-app-id" : X_APP_ID,
    "x-app-key" : X_APP_KEY,
}

SHEETY_HEADER = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

nutrition_config = {
    "query" : input("Tell me which exercises you did? "),
    "weight_kg" : WEIGHT_KG,
    "height_cm" : HEIGHT_CM,
    "age" : AGE,
    "gender" : GENDER,
}

nutrition_response = requests.post(url = NUTRITION_ENDPOINT, json = nutrition_config, headers = NUTRITION_HEADER)
nutrition_response.raise_for_status()

check_url = "https://app.100daysofpython.dev/healthz" # check whether api running before having our exercise
check_response = requests.get(url = check_url)
print(check_response.text)

nutrition_response.raise_for_status()
result = nutrition_response.json()["exercises"]

for exercise in result:
    sheet_inputs = {
        "workout" : {
        "date" : today.strftime("%d/%m/%Y"),
        "time" : today.strftime("%X"),
        "exercise" : exercise['name'].title(),
        "duration" : exercise['duration_min'],
        "calories" : exercise["nf_calories"]
        }
    }

    sheety_response = requests.post(url = SHEETY_ENDPOINT, json = sheet_inputs, headers = SHEETY_HEADER)
    sheety_response.raise_for_status()

