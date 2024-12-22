from fastapi import HTTPException, status
from db import Books


class BookService:

    @staticmethod 
    def mark_book_unavailable(book_id: str):

        if book_id not in Books:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
        
        Books[book_id]["is_available"] = False

        return Books[book_id]