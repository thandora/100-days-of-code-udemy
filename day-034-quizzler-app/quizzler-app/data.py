import requests

URL = "https://opentdb.com/api.php?"
N_QUESTIONS = 10

parameters = {
    "amount": N_QUESTIONS,
    "type": "boolean",
}

response = requests.get(url=URL, params=parameters)
question_data = response.json()["results"]
