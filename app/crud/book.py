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
    

    @staticmethod
    def update_book(db:Session, book_id: str, data: BookUpdate):
        book = BookCrud.get_book_by_id(db, book_id)

        if not book:
            return None
        
        Updated_book_dict = data.model_dump(exclude_unset=True)

        for key, value in Updated_book_dict.items():
            setattr(book, key, value)

        db.add(book)
        db.commit()
        db.refresh(book)

        return book
    

    @staticmethod
    def partially_update_book(db:Session, book_id: str, data: BookPatch):
        book = BookCrud.get_book_by_id(db, book_id)

        if not book:
            return None
        
        partially_updated_book_dict = data.model_dump(exclude_unset=True)

        for key, value in partially_updated_book_dict.items():
            setattr(book, key, value)

        db.add(book)
        db.commit()
        db.refresh(book)
        
        return book
    

    @staticmethod
    def delete_book(db:Session, book_id: str):
        book = BookCrud.get_book_by_id(db, book_id)

        if not book:
            return None
        
        db.delete(book)
        db.commit()

        return {"message": "Book deleted successfully"}
    


Book_crud = BookCrud()