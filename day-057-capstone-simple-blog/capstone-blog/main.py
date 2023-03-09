from flask import Flask, render_template
import requests

app = Flask(__name__)
blog_posts_api = "https://api.npoint.io/c790b4d5cab58020d391"
blog_posts = requests.get(blog_posts_api).json()


@app.route("/")
def home():
    return render_template("index.html", blog_posts=blog_posts)


@app.route("/post/<int:blog_id>")
def show_blog(blog_id):
    for post in blog_posts:
        if post["id"] == blog_id:
            blog_post = post
            break

    return render_template("post.html", blog_id=blog_id, blog_post=blog_post)


if __name__ == "__main__":
    app.run(debug=True)
