from uuid import uuid4
from model import User, Book, Borrow
from schemas.borrow import BorrowBase, BorrowRecord, Return
from sqlalchemy.orm import Session


class BorrowService:

    @staticmethod
    def borrow_book(db:Session, data:BorrowBase):

        user = db.query(User).filter(User.id==data.user_id).first()

        if not user and user.is_active==False:
            return None
        
        book = db.query(Book).filter(Book.id==data.book_id).first()

        if not book and book.is_available==False:
            return None
        
        borrow = Borrow(id=str(uuid4()), **data.model_dump())

        book.is_available = False

        db.add(borrow)
        db.commit()
        db.refresh(borrow)

        return borrow

    

    # @staticmethod
    # def return_book(record_id:str, data:Borrow):
    
    #     if record_id not in Borrow_Records:
    #         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Record not found")
        
    #     Borrow_Records[record_id]["return_date"] = data.return_date

    #     book_id = Borrow_Records[record_id]["book_id"]

    #     Books[book_id]["is_available"] = True

    #     return Borrow_Records[record_id] 
    
