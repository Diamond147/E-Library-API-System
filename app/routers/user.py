from fastapi import APIRouter, status, HTTPException, Depends
from schemas.user import UserCreate, UserPatch, UserUpdate, Deactivate
from crud.user import User_Crud
from model import User
from services.user import UserService
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

user_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#get all users
@user_router.get("/", status_code=status.HTTP_200_OK)
async def get_all_users(db:Session = Depends(get_db)):
    users = User_Crud.get_all_users(db)
    return {"detail": users, "message": "successful"}


#create user
@user_router.post("/", status_code=status.HTTP_201_CREATED)   
async def create_user(data:UserCreate, db:Session = Depends(get_db)):
    new_user = User_Crud.create_user(db, data)
    return {"detail": new_user, "message": "User created successfully"}


#get user by id
@user_router.get("/{user_id}", status_code=status.HTTP_200_OK)   
async def get_user_by_id(user_id:str, db:Session = Depends(get_db)):
    user = User_Crud.get_user_by_id(db, user_id)

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    return {"detail": user, "message": "successful"}


#update user
@user_router.put("/{user_id}", status_code=status.HTTP_200_OK)
async def update_user(user_id: str, data: UserUpdate, db: Session = Depends(get_db)):

    user =  User_Crud.update_user(db, user_id, data)

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    return {"detail": user, "message": "User updated successfully"}


# partially update user
@user_router.patch("/{user_id}", status_code=status.HTTP_200_OK)
async def partially_update_user(user_id: str, data:UserPatch, db:Session = Depends(get_db)):
    user =  User_Crud.partially_update_user(db, user_id, data)

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    return {"detail": user, "message": "Name updated successfully"}

#delete user
@user_router.delete("/{user_id}", status_code=status.HTTP_200_OK)
async def delete_user(user_id: str, db:Session = Depends(get_db)):
    user = User_Crud.delete_user(db, user_id)

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    return {"message": "User deleted successfully"}

#deactivate user
@user_router.put("/{user_id}/deactivate", status_code=status.HTTP_200_OK)
async def deactivate(user_id: str, data: Deactivate, db:Session = Depends(get_db)):

    user = UserService.deactivate(db, user_id, data)

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    return {"detail": user, "message": "User deactivated successfully"}
