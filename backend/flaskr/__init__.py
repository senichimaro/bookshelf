import os
import sys
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy  # , or_
from flask_cors import CORS
import random

from models import setup_db, Book, db

BOOKS_PER_SHELF = 8


def paginate_books(request, items):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * BOOKS_PER_SHELF
    end = start + BOOKS_PER_SHELF

    books = [book.format() for book in items]
    current_list = books[start:end]

    return current_list

# @TODO: General Instructions
#   - As you're creating endpoints, define them and then search for 'TODO' within the frontend to update the endpoints there.
#     If you do not update the endpoints, the lab will not work - of no fault of your API code!
#   - Make sure for each route that you're thinking through when to abort and with which kind of error
#   - If you change any of the response body keys, make sure you update the frontend to correspond.


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    # CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type,Authorization,true"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS"
        )
        return response

    # @TODO: Write a route that retrivies all books, paginated.
    #         You can use the constant above to paginate by eight books.
    #         If you decide to change the number of books per page,
    #         update the frontend to handle additional books in the styling and pagination
    #         Response body keys: 'success', 'books' and 'total_books'
    # TEST: When completed, the webpage will display books including title, author, and rating shown as stars
    @app.route('/', methods=['GET'])
    def index():
        # get all books
        books = Book.query.order_by('id').all()
        # pagination
        page = request.args.get('page', 1, type=int)
        books_formated = paginate_books(request, books)

        # return response
        return jsonify({
            "success": True,
            "books": books_formated,
            "total_books": len(books),
            "books_per_page": len(books_formated),
            "page": page
        })

    # @TODO: Write a route that will update a single book's rating.
    #         It should only be able to update the rating, not the entire representation
    #         and should follow API design principles regarding method and route.
    #         Response body keys: 'success'
    # TEST: When completed, you will be able to click on stars to update a book's rating and it will persist after refresh
    @app.route('/books/<int:book_id>', methods=['PATCH'])
    def update_rating(book_id):

        # get body
        body = request.get_json()

        # get book by id
        try:
            # find book
            book = Book.query.filter(Book.id == book_id).one_or_none()
            if book is None:
                abort(404)

            # update rating
            if "rating" in body:
                book.rating = int(body.get('rating'))

            book.update()

            return jsonify({
                "success": True,
                "message": "Rating Updated"
            })

        except:
            abort(400)

    # @TODO: Write a route that will delete a single book.
    #        Response body keys: 'success', 'deleted'(id of deleted book), 'books' and 'total_books'
    #        Response body keys: 'success', 'books' and 'total_books'
    # TEST: When completed, you will be able to delete a single book by clicking on the trashcan.

    # @TODO: Write a route that create a new book.
    #        Response body keys: 'success', 'created'(id of created book), 'books' and 'total_books'
    # TEST: When completed, you will be able to a new book using the form. Try doing so from the last page of books.
    #       Your new book should show up immediately after you submit it at the end of the page.

    @app.route('/books', methods=['POST'])
    def create_book():
        # get body request
        body = request.get_json()
        newtitle = body.get('title', None)
        newauthor = body.get('author', None)
        newrating = body.get('rating', None)

        # create pattern
        error = False
        try:
            book = Book(
                title=newtitle,
                author=newauthor,
                rating=newrating
                )
            book.insert()
        except:
            error = True
            db.session.rollback()
            print(sys.exc_info())
        finally:
            db.session.close()

        if error:
            abort(400)
        else:
            return jsonify({"message": "Book succesfully created", "success": True})


    return app
