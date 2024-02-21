import requests
import datetime

APP_ID = "93d751c8"
api_key = "bf1894d4bd041b0f59ba31b71790abef"

#using the NLP for exercise api
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
header = {
    "x-app-id" : APP_ID,
    "x-app-key" : api_key
}
exercise_text = input("Tell me what exercises did you manage to do?")
parameters = {
    "query" : exercise_text
}
exercise_response = requests.post(url=exercise_endpoint, json=parameters, headers=header)
my_exercise = exercise_response.json()

today = datetime.date.today()
time = datetime.datetime.now()
t1 = time.strftime("%H:%M:%S")
d1 = today.strftime("%d/%m/%Y")
ex = my_exercise["exercises"][0]["user_input"]
duration = my_exercise["exercises"][0]["duration_min"]
cal = my_exercise["exercises"][0]["nf_calories"]
sheet_parameters = {"sheet1" : {
    "date" : d1,
    "time" : t1,
    "exercise" : ex,
    "duration" : duration,
    "calories" : cal
}}
headers ={
    "authorization" : "Basic cGF2a291c2hpazpiZXJpZ2h0MDA4QDEyMw=="
}
sheet_endpoint ="https://api.sheety.co/0a52c0bda43a47250fa2e63138ec6a8a/myWorkout/sheet1"
sheet_responose = requests.post(url=sheet_endpoint, json=sheet_parameters, headers=headers)


