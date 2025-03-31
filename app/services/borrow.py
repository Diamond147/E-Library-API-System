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
    

# #from sqlalchemy.orm import Session
# from fastapi import Depends, HTTPException, status
# from database import SessionLocal
# from models import User, Book, BorrowRecord
# import uuid
# from datetime import datetime

# # Dependency to get the database session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# def borrow_book(user_id: str, book_id: str, db: Session = Depends(get_db)):
#     # Check if user exists
#     user = db.query(User).filter(User.id == user_id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
#     if not user.is_active:
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User is not active")

#     # Check if book exists
#     book = db.query(Book).filter(Book.id == book_id).first()
#     if not book:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    
#     if not book.is_available:
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Book is not available")

#     # Create a borrow record
#     record = BorrowRecord(
#         id=str(uuid.uuid4()),
#         user_id=user_id,
#         book_id=book_id,
#         borrow_date=datetime.utcnow(),
#         return_date=None
#     )

#     # Update book availability
#     book.is_available = False

#     # Save changes to the database
#     db.add(record)
#     db.commit()
#     db.refresh(record)

#     return record

    

    @staticmethod
    def return_book(record_id:str, data:Borrow):
    
        if record_id not in Borrow_Records:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Record not found")
        
        Borrow_Records[record_id]["return_date"] = data.return_date

        book_id = Borrow_Records[record_id]["book_id"]

        Books[book_id]["is_available"] = True

        return Borrow_Records[record_id] 
    
