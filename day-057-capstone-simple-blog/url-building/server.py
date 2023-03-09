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


@app.route("/blog/<number>")
def get_blog(number):
    # API
    blog_api = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_r = requests.get(url=blog_api)
    blog_posts = blog_r.json()

    return render_template("blog.html", blog_posts=blog_posts)


if __name__ == "__main__":
    app.run(debug=True)
