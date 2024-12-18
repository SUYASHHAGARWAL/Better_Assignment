import unittest
from app import app

class LibraryTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_book(self):
        response = self.app.post('/books/', json={'title': 'Book 1', 'author': 'Author 1'})
        self.assertEqual(response.status_code, 201)

    def test_get_books(self):
        response = self.app.get('/books/')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
