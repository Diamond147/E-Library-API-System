from uuid import uuid4
from schemas.book import Book,BookCreate,BookPatch,BookUpdate
from model import Book
from sqlalchemy.orm import Session


class BookCrud:
    
    @staticmethod
    def get_all_books(db:Session):
        return db.query(Book).all()
    

    @staticmethod
    def create_book(db:Session, data: BookCreate):
            
        book_id = str(uuid4())
        new_book = Book(id = book_id, **data.model_dump())
        # new_book = Book(**data.model_dump())

        db.add(new_book)
        db.commit()
        db.refresh(new_book)

        return new_book
    
    
    @staticmethod
    def get_book_by_id(db:Session, book_id:str):
        return db.query(Book).filter(Book.id == book_id).first()
    

    # @staticmethod
    # def update_book(book_id: str, data: BookUpdate):

    #     if book_id not in Books:
    #         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
        
    #     Books[book_id] = data.model_dump()

    #     return Books[book_id]
    

    # @staticmethod
    # def partially_update_book(book_id: str, data: BookPatch):

    #     if book_id not in Books:
    #         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
        
    #     Books[book_id] = data.model_dump(exclude_unset=True)

    #     return Books[book_id]
    

    # @staticmethod
    # def delete_book(book_id: str):

    #     if book_id not in Books:
    #         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
        
    #     del Books[book_id]

    #     return {"message": "Book deleted successfully"}
    


Book_crud = BookCrud()