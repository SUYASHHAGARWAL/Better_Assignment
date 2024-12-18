from flask import Flask, Blueprint, request, jsonify

# Create Flask app
app = Flask(__name__)

# Static list of books and members (simulated databases)
books = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"id": 3, "title": "1984", "author": "George Orwell"}
]

members_db = [
    {"id": 1, "name": "John Doe", "email": "john.doe@example.com"},
    {"id": 2, "name": "Jane Smith", "email": "jane.smith@example.com"}
]

# Define blueprints
book_routes = Blueprint('book_routes', __name__)
member_routes = Blueprint('member_routes', __name__)

# Book Routes
@book_routes.route('/', methods=['POST'])
def create_book():
    data = request.get_json()
    new_book = {
        'id': len(books) + 1,
        'title': data['title'],
        'author': data['author']
    }
    books.append(new_book)
    return jsonify(new_book), 201

@book_routes.route('/', methods=['GET'])
def get_books():
    return jsonify(books)

@book_routes.route('/<int:book_id>/', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404

@book_routes.route('/<int:book_id>/', methods=['PUT'])
def update_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if not book:
        return jsonify({"message": "Book not found"}), 404
    data = request.get_json()
    book['title'] = data['title']
    book['author'] = data['author']
    return jsonify(book)

@book_routes.route('/<int:book_id>/', methods=['DELETE'])
def delete_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book:
        books.remove(book)
        return jsonify({"message": "Book deleted"})
    return jsonify({"message": "Book not found"}), 404

# Member Routes
@member_routes.route('/', methods=['POST'])
def create_member():
    data = request.get_json()
    new_member = {
        'id': len(members_db) + 1,
        'name': data['name'],
        'email': data['email']
    }
    members_db.append(new_member)
    return jsonify(new_member), 201

@member_routes.route('/', methods=['GET'])
def get_members():
    return jsonify(members_db)

@member_routes.route('/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = next((member for member in members_db if member["id"] == member_id), None)
    if member:
        return jsonify(member)
    return jsonify({"message": "Member not found"}), 404

# Register blueprints with Flask app
app.register_blueprint(book_routes, url_prefix='/books')
app.register_blueprint(member_routes, url_prefix='/members')

if __name__ == '__main__':
    app.run(debug=True)
