books = []
members_db = []

def get_book_by_id(book_id):
    return next((book for book in books if book['id'] == book_id), None)

def get_member_by_id(member_id):
    return next((member for member in members_db if member['id'] == member_id), None)
