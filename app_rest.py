from flask import Flask, request, jsonify,abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean, or_
from flask_jwt_extended import create_access_token, jwt_required
from werkzeug.exceptions import HTTPException




import os
from flask_jwt_extended import JWTManager


app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['JWT_SECRET_KEY'] = 'BFBA2002'  # Change this!
jwt = JWTManager(app)
db = SQLAlchemy(app)

#book entity
class Book(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    poster = Column(String(200))
    summary = Column(String(500))
    is_available = Column(Boolean, default=True)
    author_name = Column(String(50))
    author_country = Column(String(50))

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
# with app.app_context():
#     db.create_all()




# This decorator tells Flask to use this function when an exception occurs
@app.errorhandler(Exception)
def handle_error(e):
    # Default status code is 500, which means Internal Server Error
    code = 500
    # If the exception is an HTTPException (which includes most types of HTTP errors)
    if isinstance(e, HTTPException):
        # Use the HTTP status code from the exception
        code = e.code
    # Return a JSON response with the error message and the status code
    return jsonify(error=str(e)), code

# This decorator tells Flask to use this function when a 404 error occurs
@app.errorhandler(404)
def handle_not_found(e):
    # Return a JSON response with the error message and the status code 404
    return jsonify(error=str(e)), 404

@app.route('/')
def index():
    return jsonify([{'name': 'alice',
                       'email': 'alice@outlook.com'},{'name': 'alice',
                       'email': 'alice@outlook.com'},{'name': 'alice',
                       'email': 'alice@outlook.com'},{'name': 'alice',
                       'email': 'alice@outlook.com'}])


#connection pour recevoir le token
@app.route('/api/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    # TODO: vérifiez l'username et le mot de passe avec votre base de données ici
    if username != 'test' or password != 'test':
        return jsonify({'login': False}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)


# Endpoint for creating a new book
@app.route('/api/book', methods=['POST'],endpoint='create_book')
@jwt_required()
def create_book():
    # Get the request data
    data = request.get_json()
    # Create a new Book object
    new_book = Book(title=data['title'], poster=data['poster'], summary=data['summary'], is_available=data['is_available'], author_name=data['author_name'], author_country=data['author_country'])
    # Add the new book to the session
    db.session.add(new_book)
    # Commit the session to save the book
    db.session.commit()
    # Return a success message
    return jsonify({'message': 'New book created.'}), 201

# Endpoint for getting the list of books
@app.route('/api/book', methods=['GET'],endpoint='get_books')
def get_books():
    # Get the query parameters
    query = request.args
    # Query the database for books
    filter_condition = or_(*[Book.__table__.columns[key].ilike(f"%{value}%") for key, value in query.items()])
    books = Book.query.filter(filter_condition).all()
    # Convert the list of books to JSON
    books_json = [book.to_dict() for book in books]
    # Return the list of books
    return jsonify(books_json), 200

# Endpoint for getting a book by id
@app.route('/api/book/<int:book_id>', methods=['GET'],endpoint='get_book')
@jwt_required()
def get_book(book_id):
    # Get the book by id
    book = Book.query.get(book_id)
    # If the book is not found, return a 404 error
    if book is None:
        abort(404, description="Book not found")
    # Convert the book to JSON
    book_json = book.to_dict()
    # Return the book
    return jsonify(book_json), 200



# Endpoint for updating a book
@app.route('/api/book/<int:book_id>', methods=['PUT'],endpoint='update_book')
@jwt_required()
def update_book(book_id):
    # Get the request data
    data = request.get_json()
    # If required attributes are missing, return a 400 error
    if 'title' not in data or 'author' not in data:
        abort(400, description="Missing required attributes")
    # Get the book to update
    book = Book.query.get(book_id)
    # If the book is not found, return a 404 error
    if book is None:
        abort(404, description="Book not found")
    # Update the book's fields
    for key, value in data.items():
        setattr(book, key, value)
    # Commit the session to save the changes
    db.session.commit()
    # Return a success message
    return jsonify({'message': 'Book updated.'}), 200



# Endpoint for deleting a book
@app.route('/api/book/<int:book_id>', methods=['DELETE'],endpoint='delete_book')
@jwt_required()
def delete_book(book_id):
    # Get the book to delete
    book = Book.query.get(book_id)
    # If the book is not found, return a 404 error
    if book is None:
        abort(404, description="Book not found")
    # Delete the book
    db.session.delete(book)
    # Commit the session to save the changes
    db.session.commit()
    # Return a success message
    return jsonify({'message': 'Book deleted.'}), 200


if __name__ == '__main__':
    app.run(debug=True)



# from app import create_app

# app = create_app()

# if __name__ == "__main__":
#     app.run(debug=True)