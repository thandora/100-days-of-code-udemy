from flask import Flask, render_template
import random
from datetime import datetime
import requests

# Flask Server
app = Flask(__name__)


@app.route("/")
def home():
    rand_number = random.randint(1, 8)
    current_year = datetime.now().year
    creator = "John Doe"
    return render_template(
        "index.html", num=rand_number, year=current_year, creator=creator
    )


@app.route("/guess/<name>/")
def guess_name(name):
    # API
    age_api = "https://api.agify.io"
    gender_api = "https://api.genderize.io"
    parameters = {
        "name": name,
    }

    age_r = requests.get(url=age_api, params=parameters)
    gender_r = requests.get(url=gender_api, params=parameters)
    age_r.raise_for_status()
    gender_r.raise_for_status()

    predicted_gender = gender_r.json()["gender"]
    predicted_age = age_r.json()["age"]

    return render_template(
        "guess.html", gender=predicted_gender, age=predicted_age, name=name
    )


@app.route("/guess/")
def guess():
    return "<h1>I will try to guess your gender and age, enter your name through URL: '/guess/&ltNAME&gt</h1>"


if __name__ == "__main__":
    app.run(debug=True)
