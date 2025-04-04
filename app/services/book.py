from sqlalchemy.orm import Session
from crud.book import Book_crud
from schemas.book import BookUnavailable


class BookService:

    @staticmethod 
    def mark_book_unavailable(db:Session, book_id: str, data: BookUnavailable):
        book = Book_crud.get_book_by_id(db, book_id)

        if not book:
            return None
        
        book_status = data.model_dump(exclude_unset=True)

        for key, value in book_status.items():
            setattr(book, key, value)

        db.add(book)
        db.commit()
        db.refresh(book)

        return book