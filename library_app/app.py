from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# In-memory storage for books
books = {}
next_id = 1

# Home route (optional)
@app.route('/')
def home():
    return "<h2>Welcome to the Library Book Management System</h2><a href='/books_view'>View All Books</a>"

# Get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(list(books.values()))

# Get a book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = books.get(book_id)
    if book:
        return jsonify(book)
    return jsonify({'error': 'Book not found'}), 404

# Search by author
@app.route('/books/search')
def search_books():
    author = request.args.get('author')
    if not author:
        return jsonify({'error': 'Author parameter required'}), 400
    result = [b for b in books.values() if b['author'].lower() == author.lower()]
    return jsonify(result)

# Add a new book
@app.route('/books', methods=['POST'])
def add_book():
    global next_id
    data = request.get_json()
    if not data or not all(key in data for key in ('title', 'author', 'year', 'available')):
        return jsonify({'error': 'Missing required fields'}), 400
    book = {
        'id': next_id,
        'title': data['title'],
        'author': data['author'],
        'year': data['year'],
        'available': data['available']
    }
    books[next_id] = book
    next_id += 1
    return jsonify(book), 201

# Update a book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    if book_id not in books:
        return jsonify({'error': 'Book not found'}), 404
    books[book_id].update(data)
    return jsonify(books[book_id])

# Delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    if book_id not in books:
        return jsonify({'error': 'Book not found'}), 404
    del books[book_id]
    return jsonify({'message': 'Book deleted'})

# Basic book view using embedded HTML (replaces books_details.html)
@app.route('/books_view')
def books_view():
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Library Books</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body class="container py-4">
        <h2 class="mb-4">📚 Library Book List</h2>
        <table class="table table-bordered table-striped">
            <thead class="table-dark">
                <tr>
                    <th>ID</th><th>Title</th><th>Author</th><th>Year</th><th>Status</th>
                </tr>
            </thead>
            <tbody>
                {% for book in books.values() %}
                <tr>
                    <td>{{ book.id }}</td>
                    <td>{{ book.title }}</td>
                    <td>{{ book.author }}</td>
                    <td>{{ book.year }}</td>
                    <td>{{ "Available" if book.available else "Not Available" }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </body>
    </html>
    """
    return render_template_string(html_template, books=books)

# Run app
if __name__ == '__main__':
    app.run(debug=True)
