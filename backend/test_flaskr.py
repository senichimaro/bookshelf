import os
import unittest
import json

from flaskr import create_app
from models import setup_db, Book

class BookTestCase(unittest.TestCase):
    '''
        Test Class to endpoints and database testing
    '''

    def setUp(self):
        '''
        Test Variables
        '''
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "bookshelf_test"
        self.database_path = "postgresql://{}:{}@{}/{}".format(
        "student", "123", "127.0.0.1:5432", self.database_name
        )
        setup_db(self.app, self.database_path)

        self.new_book = {
            "title": "Test Book",
            "author": "Test Author",
            "rating": "5"
        }

    # ----
    def tearDown(self):
        '''
        Execute after reach test
        '''
        pass

    def test_index(self):
        res = self.client().get('/')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['total_books'], data['total_books'] >= 1)
        self.assertEqual(len(data['books']), len(data['books']) >= 1)

    def test_update_rating(self):
        res = self.client().patch("/books/3", json={"rating": 3})
        data = json.loads(res.data)
        book = Book.query.filter(Book.id == 3).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(book.format()["rating"], 3)


if __name__ == "__main__":
    unittest.main()
