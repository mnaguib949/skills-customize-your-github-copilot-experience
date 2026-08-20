# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI that exposes book data over HTTP. You will practice defining routes, accepting JSON request bodies, returning structured responses, and handling invalid requests.

## 📝 Tasks

### 🛠️ Create a Health Check Endpoint

#### Description

Set up the FastAPI application in `starter-code.py` and add a `GET /health` endpoint. This endpoint should let a client quickly confirm that the API is running.

#### Requirements

Completed program should:

- Create a FastAPI application
- Return a JSON response from `GET /health`
- Include a status value of `"ok"` in the response
- Start locally with Uvicorn and respond at `http://127.0.0.1:8000`

Example response:

```json
{"status": "ok"}
```

### 🛠️ Build Book CRUD Routes

#### Description

Use the in-memory `books` list in the starter code to create routes for listing, viewing, adding, and deleting books. Each book should have an integer `id`, a `title`, and an `author`.

#### Requirements

Completed program should:

- Return all books from `GET /books`
- Return one book from `GET /books/{book_id}`
- Add a book with `POST /books` using a JSON body containing `title` and `author`
- Assign a new unique integer ID when a book is added
- Delete a book with `DELETE /books/{book_id}`
- Return an appropriate response when a requested book does not exist

Example request body:

```json
{"title": "The Hobbit", "author": "J.R.R. Tolkien"}
```

### 🛠️ Add Validation and Error Handling

#### Description

Improve the API by defining Pydantic models for incoming and outgoing book data. Use validation and HTTP errors to make the API predictable for clients.

#### Requirements

Completed program should:

- Require a non-empty `title` and `author` when creating a book
- Reject invalid request data with FastAPI's validation response
- Return status code `404` when a book ID cannot be found
- Return status code `201` after successfully creating a book
- Return the created book in the `POST /books` response
- Use FastAPI's automatic `/docs` page to test each route

Stretch goal: add `PUT /books/{book_id}` to update an existing book's title and author.
