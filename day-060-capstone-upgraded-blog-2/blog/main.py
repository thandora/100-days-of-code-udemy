from flask import Flask, render_template, request
import requests
from datetime import datetime
from dotenv import load_dotenv
import os
import smtplib


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


@app.route("/post/<int:blog_id>")
def show_post(blog_id: int):
    selected_post = None
    for post in posts:
        if post["id"] == blog_id:
            selected_post = post

    return render_template("post.html", post=selected_post, current_year=current_year)


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "GET":
        header_message = "Contact Me"

    elif request.method == "POST":
        # Env vars
        load_dotenv(".env")
        SITE_EMAIL = os.getenv("SITE_EMAIL")
        SITE_EMAIL_PASS = os.getenv("SITE_EMAIL_PASS")

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            user_name = request.form["name"]
            user_email = request.form["email"]
            user_phone = request.form["phone_number"]
            user_message = request.form["message"]

            message = f"Subject: Site Message\n\nFrom: {user_name}, {user_phone}\nEmail: {user_email}\n{user_message}"

            connection.starttls()
            connection.login(user=SITE_EMAIL, password=SITE_EMAIL_PASS)
            connection.sendmail(from_addr=SITE_EMAIL, to_addrs=SITE_EMAIL, msg=message)

        header_message = "Successfully Sent Message"

    return render_template(
        "contact.html", current_year=current_year, header_message=header_message
    )


@app.route("/sent", methods=["POST"])
def send_message():
    pass


if __name__ == "__main__":
    app.run(debug=True)
