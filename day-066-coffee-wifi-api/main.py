from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import sample
from pprint import pprint


app = Flask(__name__)

# #Connect to Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {
            column.name: getattr(self, column.name) for column in self.__table__.columns
        }


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/all")
def all_cafe():
    with app.app_context():
        cafes_raw = db.session.query(Cafe).all()
        cafes = [cafe.to_dict() for cafe in cafes_raw]
        pprint(cafes)

    return jsonify(cafes=cafes, count=len(cafes))


# HTTP GET - Read Record
@app.route("/random")
def random_cafe():
    with app.app_context():
        cafes = db.session.query(Cafe).all()
        random_cafe = sample(population=cafes, k=1)[0]
        print(random_cafe)
        return jsonify(cafe=dict(random_cafe.to_dict()))


# HTTP GET - Read Record
@app.route("/search")
def search_cafe():
    loc = request.args.get("loc")

    with app.app_context():
        result = db.session.query(Cafe).filter_by(location=loc).all()
        if result:
            result = [cafe.to_dict() for cafe in result]
            count = len(result)
        else:
            result = {"Not Found": "Sorry, we don't have a cafe at that location"}
            count = 0

        return jsonify(cafe=result, count=count)


# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_cafe():
    api = request.args.get("api-key")
    if api == "TopSecretAPIKey":
        new_cafe = Cafe(
            name=request.form.get("name"),
            map_url=request.form.get("map_url"),
            img_url=request.form.get("img_url"),
            location=request.form.get("loc"),
            has_sockets=bool(request.form.get("sockets")),
            has_toilet=bool(request.form.get("toilet")),
            has_wifi=bool(request.form.get("wifi")),
            can_take_calls=bool(request.form.get("calls")),
            seats=request.form.get("seats"),
            coffee_price=request.form.get("coffee_price"),
        )
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify(
            response={
                "success": "Successfully added the new cafe.",
                "cafe": new_cafe.to_dict(),
            }
        )

    else:
        return (
            jsonify(
                error={
                    "Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."
                }
            ),
            403,
        )


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id: int):
    new_price = request.args.get("new_price")
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe is None:
        return jsonify({"error": "Cafe not found"}), 404

    cafe.coffee_price = new_price
    db.session.commit()
    return jsonify(success="Coffee price updated successfully")


# # HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id: int):
    api = request.args.get("api-key")
    cafe_to_delete = db.session.get(Cafe, cafe_id)

    if api == "TopSecretAPIKey":
        if cafe_to_delete is None:
            return (
                jsonify(
                    error={
                        "Not Found": "Sorry, a cafe with that id was not found in the database."
                    }
                ),
                404,
            )
        cafe_name = cafe_to_delete.name
        db.session.delete(cafe_to_delete)
        db.session.commit()
        return jsonify(
            success=f"'{cafe_name}' has been deleted",
            deleted_cafe=cafe_to_delete.to_dict(),
        )

    # Incorrect API
    else:
        return (
            jsonify(
                error={
                    "Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."
                }
            ),
            403,
        )


if __name__ == "__main__":
    app.run(debug=True)
