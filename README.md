# E-Library-API-System

E-Library API System


Description:

The goal of this project is to create a simple API for managing an online library system. This system allows users to borrow and return books, manage user information, and track the availability of books. 

This project uses in-memory data structures for storage and it is built with FastAPI.
## Features

User Management:

1. Create, read, update, and delete users.

2. Deactivate user accounts.

3. User status validation.

Book Management:

1. Create, read, update, and delete books.

2. Mark book as unavailable for borrowing.

3. Validate book availability.

Borrowing Operations:

1. Borrow available books for active users.

2. Return borrowed books and update the 
availability.

3. Same book cannot be borrowed by a user. 

Borrow Record Management:

1. View borrowing records for a specific user.

2. View all borrowing records.


## Tech Stack

1. Framework: FastAPI

2. Language: Python

3. Data Storage: In-memory structures (dictionaries)
## Installation

1. Python 3.9 or higher

2. pip package manager
    
## Steps

1. Clone the repository:

git clone https://github.com/taofeekadisa/e-library-api-system.git

2. Create a virtual environment:

\\\python -m venv venv\\\\

\\\source venv/bin/activate\\\

On windows

\\\python -m venv venv\\\

\\\source venv/Scripts/activate\\\

3. Install dependencies:

\\\pip install -r requirements.txt\\\ 

4. Run the FastAPI server:

\\\uvicorn main:app --reload\\\

5. Open the API documentation in your browser:

Swagger UI : http://127.0.0.1:8000/docs

Redoc: http://127.0.0.1:8000/redoc
## API Endpoints

User Endpoints

GET /v1/users/ - Get users.

POST /v1/users/ - create users.

GET /v1/users/{user_id} - Get a user by ID.

PUT /v1/users/{user_id} - Update user details.

PATCH /v1/users/{user_id} - Partially Update user details.

DELETE /v1/users/{user_id} - Delete a user.

PUT /v1/users/{user_id}/deactivate - Deactivate User

Book Endpoints

GET /v1/users/ - Get books.

POST /v1/users/ - create book.

GET /v1/users/{user_id} - Get a book by ID.

PUT /v1/users/{user_id} - Update book details.

PATCH /v1/users/{user_id} - Partially Update book details.

DELETE /v1/users/{user_id} - Delete a book.

PUT /v1/users/{user_id}/unavailable - Mark book as unavailable

Borrow Endpoints

POST /v1/borrow/{user_id}/{book_id} - Borrow a book.

POST /v1/borrow/{user_id}/{book_id}- Book not available

PATCH /v1/borrow/{book_id} -Borrowed book status

PUT /v1/borrow/{book_id} - Book cannot be Borrowed

PATCH /v1/borrow/return/{record_id} -Return book

BorrowRecord Endpoints

GET /v1/borrowrecord/{user_id} - View specific book record.

GET /v1/borrowrecord/- View all borroe records.
## Running Tests

To run the tests, execute the following command:

\\\pytest\\\


## Contributing

Contributions are welcome! Please follow these steps:

Fork the repository.

Create a new branch.

Commit your changes.

Push to the branch.

Open a Pull Request.
