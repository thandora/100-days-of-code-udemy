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
    return render_template("index.html")


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, user_id)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":

        password = request.form.get("password")

        secure_pass = generate_password_hash(
            password=password, method="pbkdf2:sha256", salt_length=8
        )
        new_user = User(
            email=request.form.get("email"),
            name=request.form.get("name"),
            password=secure_pass,
        )

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("secrets", name=new_user.name))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        email = request.form.get("email")
        user = User.query.filter_by(email=email).first()

        if user:
            password = user.password
            form_password = request.form.get("password")
            if check_password_hash(pwhash=password, password=form_password):
                login_user(user, remember=False)
                return redirect(url_for("secrets"))

    return render_template("login.html")


@app.route("/secrets")
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name)


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


@app.route("/click")
def click():
    x = User.query.filter_by(email="qqq").first()
    userera = User.query.filter_by(email="quin@email.com").first()

    print(f"is active: {userera.is_authenticated}")
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
