from fastapi import APIRouter, status
from schemas.user import UserCreate, UserPatch, UserUpdate
from crud.user import User_Crud
from db import Users
from services.user import UserService


user_router = APIRouter()

#get all users
@user_router.get("/", status_code=status.HTTP_200_OK)
async def get_users(): 
    return {"detail": Users, "message": "successful"}

#create user
@user_router.post("/", status_code=status.HTTP_201_CREATED)   
async def create_user(data:UserCreate):
    user = User_Crud.create_user(data)
    return {"detail": user, "message": "User created successfully"}

#get user by id
@user_router.get("/{user_id}", status_code=status.HTTP_200_OK)   
async def get_user_by_id(user_id:str):
    user = User_Crud.get_user_by_id(user_id)
    return {"detail": user, "message": "successful"}

#update user
@user_router.put("/{user_id}", status_code=status.HTTP_200_OK)
async def update_user(user_id: str, data: UserUpdate):
    user =  User_Crud.update_user(user_id, data)
    return {"detail": user, "message": "User updated successfully"}

# partially update user
@user_router.patch("/{user_id}", status_code=status.HTTP_200_OK)
async def partially_update_user(user_id: str, data:UserPatch):
    user =  User_Crud.partially_update_user(user_id, data)
    return {"detail": user, "message": "Name updated successfully"}

#delete user
@user_router.delete("/{user_id}", status_code=status.HTTP_200_OK)
async def delete_user(user_id: str):
    User_Crud.delete_user(user_id)
    return {"message": "User deleted successfully"}

#deactivate user
@user_router.put("/{user_id}/deactivate", status_code=status.HTTP_200_OK)
async def deactivate(user_id: str):
    user = UserService.deactivate(user_id)
    return {"detail": user, "message": "User deactivated successfully"}
