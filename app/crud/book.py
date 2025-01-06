from fastapi import HTTPException, status
from schemas.book import Book,BookCreate,BookPatch,BookUpdate
from uuid import uuid4
from db import Books


class BookCrud:
    
    @staticmethod
    def get_books():
            return Books
    

    @staticmethod
    def create_book(data: BookCreate):
        
        for id, var in Books.items():
            if var["author"] == data.author and var["title"] == data.title:
                raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Book already exist")
            
        id = str(uuid4())
        new_book = Book(book_id = id, **data.model_dump())
        Books[id] = new_book.model_dump()

        return new_book
    
    
    @staticmethod
    def get_book_by_id(book_id:str):
        if book_id not in Books:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
        
        return Books[book_id]
    

    @staticmethod
    def update_book(book_id: str, data: BookUpdate):

        if book_id not in Books:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
        
        Books[book_id] = data.model_dump()

        return Books[book_id]
    

    @staticmethod
    def partially_update_book(book_id: str, data: BookPatch):

        if book_id not in Books:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
        
        Books[book_id] = data.model_dump(exclude_unset=True)

        return Books[book_id]
    

    @staticmethod
    def delete_book(book_id: str):

        if book_id not in Books:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
        
        del Books[book_id]

        return {"message": "Book deleted successfully"}
    


Book_crud = BookCrud()