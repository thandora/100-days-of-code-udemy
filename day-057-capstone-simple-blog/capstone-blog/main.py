from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)
blog_posts_api = "https://api.npoint.io/c790b4d5cab58020d391"
blog_posts_raw = requests.get(blog_posts_api).json()

# Store blog posts as Post objects.
posts = []
for post in blog_posts_raw:
    blog_id = post["id"]
    title = post["title"]
    subtitle = post["subtitle"]
    body = post["body"]
    blog_post = Post(blog_id=blog_id, title=title, subtitle=subtitle, body=body)
    posts.append(blog_post)


@app.route("/")
def home():
    return render_template("index.html", blog_posts=posts)


@app.route("/post/<int:blog_id>")
def show_blog(blog_id):
    for post in posts:
        if post.id == blog_id:
            blog_post = post
            break

    return render_template("post.html", blog_id=blog_id, blog_post=blog_post)


if __name__ == "__main__":
    app.run(debug=True)
