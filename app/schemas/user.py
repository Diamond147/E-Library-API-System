from typing import Optional
from uuid import UUID
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    name: str = "Opeyemi"
    email: EmailStr = "email1@gmail.com"
    is_active: bool = True 

class User(UserBase):
    id: UUID  

class UserCreate(UserBase):
    pass 

class UserUpdate(BaseModel):
    name: Optional[str] = "Williams"
    email: Optional[EmailStr] = "email11@gmail.com"
    is_active: bool = True 

class UserPatch(BaseModel):
    name: Optional[str] = "Johnson"
    email: Optional[EmailStr] = "email11@gmail.com"
    is_active: bool = True

class Deactivate(BaseModel):
    name: Optional[str] = "Johnson"
    email: Optional[EmailStr] = "email11@gmail.com"
    is_active: bool = False