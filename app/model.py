from sqlalchemy import String, Boolean, Integer
from sqlalchemy.orm import Mapped, mapped_column
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False, server_default="Unknown")
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, email={self.email!r}, age={self.age!r}, is_active={self.is_active!r})"
    
# server_default ensures a default value is set at the database level, even for existing rows. This is for Alembic migrations.

class Book(Base):
    __tablename__ = "books"

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    title: Mapped[str] = mapped_column(String)
    author: Mapped[str] = mapped_column(String)
    is_available: Mapped[bool] = mapped_column(Boolean, default=True) 

    def __repr__(self) -> str:
        return f"Book(id={self.id!r}, title={self.title!r}, author={self.author!r}, is_available={self.is_available!r})"


# class Borrow(Base):
#     __tablename__ = "borrows"

    # id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
#     user_id: Mapped[uuid4] = mapped_column(ForeignKey("users.id"))
#     book_id: Mapped[uuid4] = mapped_column(ForeignKey("books.id"))
#     return_date: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now)

#     def __repr__(self) -> str:
#         return f"Borrow(id={self.id!r}, user_id={self.user_id!r}, book_id={self.book_id!r}, return_date={self.return_date!r})"