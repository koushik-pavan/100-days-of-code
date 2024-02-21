import requests

question_data = requests.get(url="https://opentdb.com/api.php?amount=10&category=11&type=boolean")
question_data = question_data.json()["results"]
