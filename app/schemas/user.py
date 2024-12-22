from typing import Optional
from uuid import UUID
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str = "Opeyemi"
    email: str = "email1@gmail.com"

class User(UserCreate):
    user_id: UUID  
    is_active: bool = True 

class UserUpdate(BaseModel):
    name: Optional[str] = "Williams"
    email: Optional[str] = "email2@gmail.com"

class UserPatch(BaseModel):
    name: Optional[str] = "Johnson"
    email: Optional[str] = "email2@gmail.com"