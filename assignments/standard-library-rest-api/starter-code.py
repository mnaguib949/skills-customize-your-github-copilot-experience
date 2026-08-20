"""Starter code for the REST APIs with Python's standard library assignment."""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse


HOST = "127.0.0.1"
PORT = 8000

books = [
    {"id": 1, "title": "A Wrinkle in Time", "author": "Madeleine L'Engle"},
    {"id": 2, "title": "The Giver", "author": "Lois Lowry"},
]


class BookCatalogHandler(BaseHTTPRequestHandler):
    """Handle requests for the book catalog API."""

    def send_json(self, status_code, payload):
        """Send a JSON response with the required HTTP headers."""
        pass

    def read_json_body(self):
        """Read and decode a JSON request body."""
        pass

    def find_book(self, book_id):
        """Return a book by ID, or None when it does not exist."""
        pass

    def do_GET(self):
        """Handle health checks and book lookup requests."""
        path = urlparse(self.path).path

        if path == "/health":
            pass
        elif path == "/books":
            pass
        elif path.startswith("/books/"):
            pass
        else:
            self.send_json(404, {"error": "Route not found"})

    def do_POST(self):
        """Create a new book from a JSON request body."""
        pass

    def do_DELETE(self):
        """Stretch goal: delete a book by ID."""
        self.send_json(405, {"error": "DELETE is a stretch goal"})

    def do_PUT(self):
        """Report that updating books is not supported."""
        self.send_json(405, {"error": "Method not allowed"})


if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), BookCatalogHandler)
    print(f"Book catalog API running at http://{HOST}:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server")
        server.server_close()