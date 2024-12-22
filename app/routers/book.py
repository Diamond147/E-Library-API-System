from fastapi import APIRouter, status
from schemas.book import BookCreate,BookPatch,BookUpdate
from crud.book import Book_crud
from db import Books
from services.book import BookService


book_router = APIRouter()

#get all books    
@book_router.get("/", status_code=status.HTTP_200_OK)
async def get_all_books():
    return {"detail": Books, "message": "successful"}

#create book
@book_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_book(data: BookCreate):
    book = Book_crud.create_book(data)
    return {"detail": book, "message": "Book created successfully"}

#get book by id
@book_router.get("/{book_id}", status_code=status.HTTP_200_OK)
async def get_book_by_id(book_id:str):
    book = Book_crud.get_book_by_id(book_id)
    return {"detail": book, "message": "successfully"}

#update book
@book_router.put("/{book_id}", status_code=status.HTTP_200_OK)
async def update_book(book_id: str, data: BookUpdate):
    book = Book_crud.update_book(book_id, data)
    return {"detail": book, "message": "Book updated successfully"}

# partially update book
@book_router.patch("/{book_id}", status_code=status.HTTP_200_OK)
async def partially_update_book(book_id: str, data: BookPatch):
    book = Book_crud.partially_update_book(book_id, data)
    return {"detail": book, "message": "Author updated successfully"}

#delete book
@book_router.delete("/{book_id}", status_code = status.HTTP_200_OK)
async def delete_book(book_id: str):
    Book_crud.delete_book(book_id)
    return {"message": "Book deleted successfully"}

#unavailable book
@book_router.put("/{book_id}/unavailable", status_code=status.HTTP_200_OK)
async def mark_book_unavailable(book_id: str):
    book = BookService.mark_book_unavailable(book_id)
    return {"detail": book, "message": "Book successfully marked as unavailable"}
