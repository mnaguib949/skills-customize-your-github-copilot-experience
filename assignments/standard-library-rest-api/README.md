# 📘 Assignment: REST APIs with Python's Standard Library

## 🎯 Objective

Build a small book-catalog REST API without using a web framework. You will practice HTTP request handling, JSON data, URL routing, input validation, and meaningful response status codes with Python's standard library.

## 📝 Tasks

### 🛠️ Create the HTTP Server

#### Description

Complete the `BookCatalogHandler` class so the server can respond to a health check and serve the existing in-memory book catalog.

#### Requirements

Completed program should:

- Start with `python starter-code.py` and listen on `http://127.0.0.1:8000`
- Return a JSON response containing `{"status": "ok"}` from `GET /health`
- Return the complete list of books from `GET /books`
- Set the `Content-Type` response header to `application/json`

### 🛠️ Add Book Routes

#### Description

Add routes for viewing one book and creating a new book. Read the request body as JSON and return the created book with a unique integer ID.

#### Requirements

Completed program should:

- Return one book from `GET /books/<book_id>`
- Return status code `404` when the requested book does not exist
- Accept `POST /books` with a JSON body containing `title` and `author`
- Assign a new unique integer ID and return the created book with status code `201`
- Return status code `400` when the request body is not valid JSON

Example request body:

```json
{"title": "The Hobbit", "author": "J.R.R. Tolkien"}
```

### 🛠️ Validate Requests and Handle Errors

#### Description

Make the API predictable for clients by validating book fields, handling unsupported methods, and returning useful JSON error messages.

#### Requirements

Completed program should:

- Reject requests with a missing or blank `title` or `author` using status code `400`
- Return status code `405` for unsupported HTTP methods
- Return a JSON error message for every failed request
- Set a `Content-Length` header on JSON responses
- Keep the server running so multiple requests can be tested with a browser or a tool such as `curl`

Stretch goal: add `DELETE /books/<book_id>` and remove the selected book from the catalog.
