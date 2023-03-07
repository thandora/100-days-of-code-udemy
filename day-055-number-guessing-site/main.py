from flask import Flask, render_template

app = Flask(__name__)

# congrats = 'https://media.giphy.com/media/xT8qBepJQzUjXpeWU8/giphy.gif'
# try_again = 'https://media.giphy.com/media/CoND5j6Bn1QZUgm1xX/giphy.gif'


@app.route("/")
def hello_world():
    return (
        "<h1 style='color: red'>Hello</h1><p>World!</p>"
        "<img src='https://media.giphy.com/media/xT8qBepJQzUjXpeWU8/giphy.gif' alt='congrats img'>"
    )


# ####### Style functions #########
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


# ################


# # Coding exercise
@app.route("/bye")
@make_bold
@make_underlined
@make_emphasis
def bye():
    return "Bye!"


# #########

#########################
@app.route("/correct")
def congratulate():
    pass


@app.route("/incorrect")
def incorrect():
    pass


#########################


@app.route("/about")
def about():
    return render_template("index.html")


@app.route("/<name>")
def greet(name):
    return f"Hello, {name}"


if __name__ == "__main__":
    app.run(debug=True)
