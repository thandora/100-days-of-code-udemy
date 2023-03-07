"""Create decorators that will wrap a string in bold, underline, and emphasis
HTML tags and apply it to the bye() function with the app.route decorator.
"""


from flask import Flask

app = Flask(__name__)


def make_bold(func):
    def wrapper():
        text = func()
        return f"<b>{text}</b>"

    return wrapper


def make_emphasis(func):
    def wrapper():
        text = func()
        return f"<em>{text}</em>"

    return wrapper


def make_underlined(func):
    def wrapper():
        text = func()
        return f"<u>{text}</u>"

    return wrapper


# # Coding exercise
@app.route("/bye")
@make_bold
@make_underlined
@make_emphasis
def bye():
    return "Bye!"


app.run(debug=True)
