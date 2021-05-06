import requests
from datetime import datetime

exercise_text = input("What exercise you did?\n")
GENDER = "male"
WEIGHT_KG = 60
HEIGHT_CM = 165
AGE = 20
APP_ID = "your id"
API_KEY = "your key"
SHEET_ENDPOINTS = "sheet end point"
EXERCISE_ENDPOINTS = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
response = requests.post(EXERCISE_ENDPOINTS, json=parameters, headers=headers)
result = response.json()
print(result)
now = datetime.now()
hour = now.strftime("%H")
min = now.strftime("%M")
sec = now.strftime("%S")
TIME = hour + ":" + min + ":" + sec
DATE = datetime.now().strftime("%d/%m/%Y")
print(DATE)
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": DATE,
            "time": TIME,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
print(sheet_inputs)
sheety_res = requests.post(SHEET_ENDPOINTS, json=sheet_inputs)
