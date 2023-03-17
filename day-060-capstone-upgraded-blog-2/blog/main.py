from flask import Flask, render_template
import requests
from datetime import datetime


current_year = datetime.now().year


blog_api = "https://api.npoint.io/f29c253c6fa46f740f4e"
posts = requests.get(url=blog_api).json()


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", posts=posts, current_year=current_year)


@app.route("/about")
def about():
    return render_template("about.html", current_year=current_year)


@app.route("/contact")
def contact():
    return render_template("contact.html", current_year=current_year)


@app.route("/post/<int:blog_id>")
def show_post(blog_id: int):
    selected_post = None
    for post in posts:
        if post["id"] == blog_id:
            selected_post = post

    return render_template("post.html", post=selected_post, current_year=current_year)


if __name__ == "__main__":
    app.run(debug=True)
