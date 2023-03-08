from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def show_home():
    return render_template("index.html")


# @app.route("/resume")
# def show_resume():
#     return render_template("resume.htm")


if __name__ == "__main__":
    app.run(debug=True)
