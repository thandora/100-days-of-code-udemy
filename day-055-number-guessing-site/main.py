"""A simple number guessing game (1-10, inclusive) where the user guesses
by typing out the guess to the url (e.g. if user guesses 4, they will input
http://127.0.0.1:5000/4)"""


from flask import Flask
import random


app = Flask(__name__)


@app.route("/")
def hello_world():
    return (
        "<h1 style='color: red'>Guess the number! (1 - 10)</h1>"
        "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' alt='intro img'>"
    )


random_number = random.randint(1, 10)


@app.route("/<int:guess>")
def show_guess_page(guess):
    if guess < random_number:
        message = (
            f"<h1>{guess} is too low. Try again!</h1>"
            "<img src='https://media.giphy.com/media/3oEduPoyJdFYgHx7YQ/giphy.gif' alt='low img'>"
        )

    elif guess > random_number:
        message = (
            f"<h1>{guess} is too high. Try again!</h1>"
            "<img src='https://media.giphy.com/media/LKTTAzGboJGzC/giphy.gif' alt='high img'>"
        )

    else:
        message = (
            "<h1>Congratulations! You got it!</h1>"
            "<img src='https://media.giphy.com/media/cXblnKXr2BQOaYnTni/giphy.gif' alt='congrats img'>"
        )
    return message


if __name__ == "__main__":
    app.run(debug=True)
