from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from dotenv import load_dotenv
import os
import requests


app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
db = SQLAlchemy()
db.init_app(app)
Bootstrap(app)


# DB model
class Movie(db.Model):
    # Fields
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    year = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float())
    ranking = db.Column(db.Integer())
    review = db.Column(db.String(500))
    img_url = db.Column(db.String(250))


# Run once to create db
# with app.app_context():
#     db.create_all()


# WTForms
class MovieRatingForm(FlaskForm):
    rating = StringField("Your rating out of 10")
    review = StringField("Your review", validators=[DataRequired()])
    submit = SubmitField("Submit")


class FindMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


@app.route("/")
def home():
    # Sort in descending order
    movies = Movie.query.order_by(Movie.rating).all()
    n_movies = len(movies)
    for i, movie in enumerate(movies):
        rank = n_movies - i
        movie.ranking = rank

    return render_template("index.html", movies=movies)


@app.route("/rate-movie", methods=["GET", "POST"])
def rate_movie():
    form = MovieRatingForm()
    movie_id = request.args.get("id")
    movie = db.session.get(Movie, movie_id)

    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()

        return redirect(url_for("home"))

    return render_template("edit.html", movie=movie, form=form)


@app.route("/delete-movie")
def delete_movie():
    movie_id = request.args.get("id")
    movie_to_delete = db.session.get(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()

    return redirect(url_for("home"))


@app.route("/add-movie", methods=["GET", "POST"])
def add_movie():
    form = FindMovieForm()

    if form.validate_on_submit():

        search_title = form.title.data
        load_dotenv(".env")
        API_KEY = os.getenv("API_KEY")

        API_ENDPOINT = "https://api.themoviedb.org/3/search/movie"
        parameters = {
            "query": search_title,
            "api_key": API_KEY,
        }
        r = requests.get(url=API_ENDPOINT, params=parameters).json()
        search_results = r["results"]

        return render_template("select.html", results=search_results)

    return render_template("add.html", form=form)


@app.route("/get-movie")
def get_movie():
    movie_id = request.args.get("id")

    # Retrieve movie data through moviedb API
    load_dotenv(".env")
    API_KEY = os.getenv("API_KEY")
    API_ENDPOINT = f"https://api.themoviedb.org/3/movie/{movie_id}"
    parameters = {"api_key": API_KEY}
    r = requests.get(url=API_ENDPOINT, params=parameters)
    movie_data = r.json()

    # Add to db
    img_path = movie_data["poster_path"]
    new_movie = Movie(
        title=movie_data["title"],
        year=movie_data["release_date"][:4],
        description=movie_data["overview"],
        img_url=f"https://image.tmdb.org/t/p/w500/{img_path}",
    )

    db.session.add(new_movie)
    db.session.commit()

    return redirect(url_for("rate_movie", id=new_movie.id))


if __name__ == "__main__":
    app.run(debug=True)
