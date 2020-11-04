from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.book import Book
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

books_blueprint = Blueprint("books", __name__)


# ----- MVP -----

# INDEX
@books_blueprint.route("/books", methods=["GET"])
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", all_books = books)

# DELETE
@books_blueprint.route("/books/<id>/delete", methods=["POST"])
def delete_book(id):
    book_repository.delete(id)
    return redirect("/books")


# ----- EXTENSIONS -----

# SHOW


# NEW

@books_blueprint.route("/books/new", methods=["GET"])
def new_book():
    authors = author_repository.select_all()
    return render_template("books/new.html", all_authors = authors)





# CREATE
@books_blueprint.route("/books", methods=["POST"])
def create_book():
    title = request.form["title"]
    genre = request.form["genre"]
    publisher = request.form["publisher"]
    author = request.form["author"]

    author = author_repository.select(author_id) #make author object
    book = Book(title, genre, publisher, author) # make book object up
    book_repository.save(book) # save it and add to database
    return redirect("/books") # redirect back to books page



# ----- ADVANCED EXTENSIONS -----

# EDIT


# UPDATE




