from flask import Flask
from routes import book_routes, member_routes
from auth import token_required

app = Flask(__name__)

app.register_blueprint(book_routes, url_prefix='/books')
app.register_blueprint(member_routes, url_prefix='/members')

if __name__ == '__main__':
    app.run(debug=True)
