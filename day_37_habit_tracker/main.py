import requests
from datetime import datetime
import os

# add keys to environment variable
# run > edit config > environment variables > add there.
# get env vars using below line of code
APP_ID = os.environ['APP_ID']
APP_API_KEY = os.environ['APP_API_KEY']


nutrition_endpoint = "https://trackapi.nutritionix.com//v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/0b0dd9539fb5d6a7f5dd0142a8d2ea50/gojo'sWorkouts/workouts"

user_ip = input("Tell me what exercise your did: ")

workout_params = {
    "query": user_ip,
}

workout_headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_API_KEY,
    "Authorization": "Basic bnVsbDpudWxs",
}


workout_response = requests.post(url=nutrition_endpoint, json=workout_params, headers=workout_headers)
workout = workout_response.json()['exercises']

now = datetime.now()

date = now.strftime(f'%d/%m/%Y')
time = now.strftime(f'%X')

for wk in workout:
    sheet_input = {
        'workout': {
            'date': date,
            'time': time,
            'exercise': wk['name'].title(),
            'duration': wk['duration_min'],
            'calories': wk['nf_calories']
        }
    }

    sheet_response = requests.post(url=sheety_endpoint, json=sheet_input)
    print(sheet_response.text)

