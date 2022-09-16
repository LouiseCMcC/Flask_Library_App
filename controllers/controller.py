from flask import render_template, request
from app import app
from models.book_list import books, add_new_book, delete_book
from models.book import Book

@app.route('/books')
def index():
    return render_template('index.html', title='Home', books=books)

@app.route('/books', methods=['POST'])
def add_book():
    book_title = request.form['title']
    book_author = request.form['author']
    book_genre = request.form['genre']
    checked_out = True if 'checked_out' in request.form else False 
    new_book = Book(book_title, book_author, book_genre, checked_out)

    add_new_book(new_book)
    return render_template('index.html', title='Home', books=books)

@app.route('/books', methods=['POST'])
def delete(title):
    delete_book(title)
    return render_template('index.html', title='Home', books=books)


