from typing import Dict
from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app
from routers.book import Books
from crud.book import Books
from fastapi import status
from uuid import uuid4

client = TestClient(app)

Mock_Books = {
    "60dfd9fb-4d9b-458d-8627-f41eb747e04c": {
        "title": "first title",
        "author": "first author",
        "book_id": "60dfd9fb-4d9b-458d-8627-f41eb747e04c",
        "is_available": True
    }
}


@patch("routers.book.Books", new=Mock_Books)
def test_get_all_books():
    response = client.get("/v1/books")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"detail": Mock_Books, "message": "successful"}


@patch("crud.book", Mock_Books)
@patch("crud.book.uuid4", return_value="982e7a40-0d99-408a-abd0-4095f070c22e")
def test_create_book(mock_uuid):
    create_book = {
        "title": "second title",
        "author": "second author",
        "is_available": True
    }
    expected_create_book = {
        "detail": {
        "book_id": "982e7a40-0d99-408a-abd0-4095f070c22e",
        "title": "second title",
        "author": "second author",
        "is_available": True
    }, "message": "Book created successfully"
    }

    response = client.post("/v1/books", json = create_book)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == expected_create_book


@patch("crud.book.Books", Mock_Books)
def test_get_book_by_id():

    expected_book = {
        "book_id": "60dfd9fb-4d9b-458d-8627-f41eb747e04c",
        "title": "first title",
        "author": "first author",
        "is_available": True
    }

    response = client.get("/v1/books/60dfd9fb-4d9b-458d-8627-f41eb747e04c")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["detail"] == expected_book
    assert response.json()["message"] == "successfully"


@patch("crud.book.Books", Mock_Books)
def test_updated_book():

    new_data = {
        "title": "updated first title",
        "author": "updated first author",
    }

    updated_book = {
        "detail": {
            "title": "updated first title",
            "author": "updated first author"
        }, "message": "Book updated successfully"
    }

    response = client.put("/v1/books/60dfd9fb-4d9b-458d-8627-f41eb747e04c", json = new_data)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == updated_book


@patch("crud.book.Books", Mock_Books)
def test_patch_book():

    new_data = {
        "title": "updated first title",
        "author": "corrected first author",
    }

    patched_book = {
        "detail": {
            "title": "updated first title",
            "author": "corrected first author"
        }, "message": "Author updated successfully"
    }

    response = client.patch("/v1/books/60dfd9fb-4d9b-458d-8627-f41eb747e04c", json = new_data)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == patched_book


@patch("crud.book.Books", Mock_Books)
def test_delete_book():
    response = client.delete("/v1/books/60dfd9fb-4d9b-458d-8627-f41eb747e04c")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Book deleted successfully"}


# @patch("services.book.Books", Mock_Books)
# def test_mark_book_unavailable():

#     expected_book = {
#         "book_id": "60dfd9fb-4d9b-458d-8627-f41eb747e04c",
#         "title": "first title",
#         "author": "first author",
#         "is_available": False
#     }

#     response = client.put("/v1/books/60dfd9fb-4d9b-458d-8627-f41eb747e04c/mark_book_unavailable")

#     # print(Mock_Books)
#     assert response.status_code == status.HTTP_200_OK
#     assert response.json()["detail"] == expected_book
#     assert response.json()["message"] == "Book successfully marked as unavailable"
