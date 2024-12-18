# Better_Assignment
Better_Assignment


Library Management System API

This is a Flask-based API for managing a library system. It allows users to perform CRUD operations for books and members. The API also includes optional features like search functionality, pagination, and token-based authentication.

Features
1. CRUD operations for books and members:
   - Create, read, update, and delete books and members.
2. Search functionality for books by title or author.
3. Pagination to limit the number of results in requests.
4. Token-based authentication to secure endpoints.

Technologies Used
- Flask: Python web framework for building the API.

How to Run the Project

Prerequisites
- Python 3.x

Setup Instructions
1. Clone the repository:
   git clone <your-repository-link>
   cd library_management_system

2. Install Flask:
   pip install Flask

3. Run the Flask application:
   python app.py

4. The API will be available at:
   http://localhost:5000


Design Choices
- In-memory storage: Since no third-party libraries or databases are allowed, the system uses Python lists and dictionaries to simulate a database for books and members.
- Modularization: The routes for books and members are organized in separate blueprints for better structure and maintainability.
- Token Authentication: Simple token-based authentication is implemented to secure sensitive endpoints.


Conclusion
This Flask API implementation provides basic CRUD functionality for a library management system, along with optional features like search, pagination, and authentication, all built without the use of third-party libraries.
