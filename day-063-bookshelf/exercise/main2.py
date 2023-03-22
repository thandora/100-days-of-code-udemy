"""
Emulate what we did in main.py using SQLAlchemy
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

db.init_app(app)


# Create database table
class Book(db.Model):
    # autoincrements allow new entries to be assigned new incrementing
    # primary key automatically
    # This is set to True by default.
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float(), nullable=False)

    def __repr__(self) -> str:
        return super().__repr__()


# # Save table to database
# with app.app_context():
#     db.create_all()


#


# # # 1. Create new record
# book1 = Book(title="Harry Pottah The Return", author="J. K. Rowling", rating=9.3)

# with app.app_context():
#     db.session.add(book1)
#     db.session.commit()


#


# # # 2a Read all records
# with app.app_context():
#     all_books = db.session.query(Book).all()

# for book in all_books:
#     # Note that fields can be accessed either by
#     # dot notation (book.title) or by
#     # indexing: (book["title"])
#     # difference is indexing by brackets read-only
#     # while dot notation allows for modification of field value.
#     print(book.title)

# # # 2b Read records by query (exact match)
# # Note that filter_by is an exact match filter.
# with app.app_context():
#     # Only return 1st match.
#     book = Book.query.filter_by(title="Harry Pottah").first()
#     print(book.title)

# # # 2c Read records by query (partial match)
# # In this examply, all records containing the str "Harry" will match
# with app.app_context():
#     books = Book.query.filter(Book.title.like("%Harry%"))
#     for book in books:
#         print(book.title)


#


# # # 3a Update a record by query
# with app.app_context():
#     book_to_update = Book.query.filter_by(title="Harry Potter").first()
#     book_to_update.title = "Harry Potter and the Chamber of Secrets"
#     db.session.commit()

# # # 3b Update a record by PRIMARY KEY
# with app.app_context():
#     book_id = 1
#     book_to_update = db.session.get(Book, book_id)
#     book_to_update.author = "Joking Roller"
#     db.session.commit()

with app.app_context():
    all_books = db.session.query(Book).all()
    for book in all_books:
        print(book.author)

# # # 4 Delete a record (by PRIMARY KEY)
# with app.app_context():
#     book_id = 1
#     book_to_delete = db.session.get(Book, book_id)
#     db.session.delete(book_to_delete)
#     db.session.commit()
