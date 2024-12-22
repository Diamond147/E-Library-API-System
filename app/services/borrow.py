from datetime import datetime
from uuid import uuid4
from fastapi import HTTPException, status
from schemas.borrow import Borrow
from db import Users, Books, Borrow_Records


class BorrowService:

    @staticmethod
    def borrow_book(user_id:str, book_id:str):

        if user_id not in Users:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        
        if not Users[user_id]["is_active"]:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not active")
        
        if book_id not in Books:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
        
        if not Books[book_id]["is_available"]:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not available")
        
        record_id = str(uuid4())

        Borrow_Records[record_id] = {
            "record_id": record_id,
            "user_id": user_id,
            "book_id": book_id,
            "borrow_date": datetime.now(),
            "return_date": None
        }

        Books[book_id]["is_available"] = False

        return Borrow_Records
    

    @staticmethod
    def book_not_available(user_id:str, book_id:str):

        if user_id not in Users:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        
        if book_id not in Books:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
        
        for record_id, record_data in Borrow_Records.items():
            if Borrow_Records[record_id]["user_id"] == user_id and Borrow_Records[record_id]["book_id"] == book_id:
                raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User has already borrowed this book")
        
        if not Books[book_id]["is_available"]:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not available")
        
        return {"message": "Book is available"}
    

    @staticmethod
    def borrowed_book_status(book_id:str):

        if Books[book_id]["is_available"] is True:
            Books[book_id]["is_available"] = False 

        return Books[book_id]
    

    @staticmethod
    def book_cannot_be_borrowed(book_id:str):

        if Books[book_id]["is_available"] is False:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book cannot be borrowed")
        
        return Books[book_id]
    

    @staticmethod
    def return_book(record_id:str, data:Borrow):
    
        if record_id not in Borrow_Records:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Record not found")
        
        Borrow_Records[record_id]["return_date"] = data.return_date

        book_id = Borrow_Records[record_id]["book_id"]

        Books[book_id]["is_available"] = True

        return {"message": "Borrowed book returned successfully", "data": Borrow_Records[record_id] }
    
