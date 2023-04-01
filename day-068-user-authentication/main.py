from flask import (
    Flask,
    render_template,
    request,
    url_for,
    redirect,
    flash,
    send_from_directory,
)
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    login_required,
    current_user,
    logout_user,
)


app = Flask(__name__)

app.config["SECRET_KEY"] = "any-secret-key-you-choose"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


# Line below only required once, when creating DB.
# db.create_all()


@app.route("/")
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, user_id)


@app.route("/register", methods=["GET", "POST"])
def register():
    error = None
    if request.method == "POST":
        email = request.form.get("email")
        user = User.query.filter_by(email=email).first()
        if user:
            error = "An account with that email is already registered."
            flash(error)
        else:
            password = request.form.get("password")

            secure_pass = generate_password_hash(
                password=password, method="pbkdf2:sha256", salt_length=8
            )
            new_user = User(
                email=email,
                name=request.form.get("name"),
                password=secure_pass,
            )

            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)

            return redirect(url_for("secrets", name=new_user.name))

    return render_template(
        "register.html", error=error, logged_in=current_user.is_authenticated
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        email = request.form.get("email")
        user = User.query.filter_by(email=email).first()
        if user:
            password = user.password
            form_password = request.form.get("password")
            if check_password_hash(pwhash=password, password=form_password):
                login_user(user, remember=False)
                return redirect(url_for("secrets"))
            else:
                error = "Incorrect email or password."
                flash(error)
        else:
            error = "Incorrect email or password."
            flash(error)

    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route("/secrets")
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name, logged_in=True)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/download")
@login_required
def download():
    return send_from_directory(
        directory=app.static_folder, path="files/cheat_sheet.pdf"
    )


if __name__ == "__main__":
    app.run(debug=True)
