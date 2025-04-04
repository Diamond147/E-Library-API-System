from fastapi import APIRouter, Depends, HTTPException, status
from schemas.book import BookCreate,BookPatch,BookUpdate, BookUnavailable
from crud.book import Book_crud
from services.book import BookService
from sqlalchemy.orm import Session
from database import get_db


book_router = APIRouter()
    
    
#get all books    
@book_router.get("/", status_code=status.HTTP_200_OK)
async def get_all_books(db:Session = Depends(get_db)):
    books = Book_crud.get_all_books(db)
    return {"detail": books, "message": "successful"}


#create book
@book_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_book(data: BookCreate, db: Session = Depends(get_db)):
    new_book = Book_crud.create_book(db, data)
    return {"detail": new_book, "message": "Book created successfully"}


#get book by id
@book_router.get("/{book_id}", status_code=status.HTTP_200_OK)
async def get_book_by_id(book_id:str, db:Session = Depends(get_db)):
    book = Book_crud.get_book_by_id(db, book_id)

    if book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    
    return {"detail": book, "message": "successfully"}

#update book
@book_router.put("/{book_id}", status_code=status.HTTP_200_OK)
async def update_book(book_id: str, data: BookUpdate, db:Session = Depends(get_db)):
    book = Book_crud.update_book(db, book_id, data)

    if book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    
    return {"detail": book, "message": "Book updated successfully"}


# partially update book
@book_router.patch("/{book_id}", status_code=status.HTTP_200_OK)
async def partially_update_book(book_id: str, data: BookPatch, db:Session = Depends(get_db)):
    book = Book_crud.partially_update_book(db, book_id, data)

    if book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    
    return {"detail": book, "message": "Author updated successfully"}


#delete book
@book_router.delete("/{book_id}", status_code = status.HTTP_200_OK)
async def delete_book(book_id: str, db:Session = Depends(get_db)):
    book = Book_crud.delete_book(db, book_id)

    if book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    
    return {"message": "Book deleted successfully"}


#unavailable book
@book_router.put("/{book_id}/unavailable", status_code=status.HTTP_200_OK)
async def mark_book_unavailable(book_id: str, data: BookUnavailable, db:Session = Depends(get_db)):
    book = BookService.mark_book_unavailable(db, book_id, data)

    if book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    
    return {"detail": book, "message": "Book successfully marked as unavailable"}
