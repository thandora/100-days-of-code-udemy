from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, re
import os

SECRET_KEY = "SUPER STRONGE PASS"


# class LoginForm(FlaskForm):
#     """Contact form."""

#     email = StringField(
#         "Email", [Email(message=("Not a valid email address.")), DataRequired()]
# #     )
# #     password = StringField(
#         "Password",
#         [DataRequired(), Length(min=4, message=("Your message is too short."))],
#     )
#     submit = SubmitField("Submit")


class LoginForm(FlaskForm):
    email = StringField(
        label="Email",
        validators=[
            DataRequired(),
            Email(),
        ],
    )

    password = PasswordField(
        label="Password", validators=[DataRequired(), Length(min=8)]
    )

    submit = SubmitField(label="Log In")


app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        if login_form.email.data.lower() == "admin@email.com":
            if login_form.password.data == "12345678":
                return render_template("success.html", form=login_form)
        else:
            return render_template("denied.html", form=login_form)

    return render_template("login.html", form=login_form)


if __name__ == "__main__":
    app.run(debug=True)
