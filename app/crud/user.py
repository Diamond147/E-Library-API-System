from uuid import UUID, uuid4
from schemas.user import UserCreate, UserPatch, UserUpdate
from model import User
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder


class UserCrud:

    @staticmethod    # you don't make use of self while using staticmethod
    def get_all_users(db:Session): 
        return db.query(User).all()
    

    @staticmethod
    def create_user(db:Session, data:UserCreate): 

        new_user = User(id=str(uuid4()), **data.model_dump())
        # new_user = User(**data.model_dump())

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user
    
    
    @staticmethod
    def get_user_by_id(db:Session, user_id:str):
        user = db.query(User).filter(User.id == user_id).first()
        return user
    

    @staticmethod
    def update_user(db: Session, user_id: str, data: UserUpdate):

        # Get the book by id
        user = User_Crud.get_user_by_id(db, user_id)

        if not user:
            return None
        
        # Convert to dict
        updated_user_dict = data.model_dump(exclude_unset=True)

        # Update the book in the database
        for key, value in updated_user_dict.items():
            setattr(user, key, value)

        db.add(user)
        db.commit()
        db.refresh(user)

        return user
    

    # @staticmethod
    # def update_user(db:Session, user_id: str, data:UserUpdate):
    #     # Get the user by id
    #     user = User_Crud.get_user_by_id(db, user_id)

    #     if not user:
    #         return None
        
    #     # Convert to dict
    #     updated_user_dict = data.model_dump(exclude_unset=True)
    #     existing_user = jsonable_encoder(user)

    #     # Update the user in the database
    #     for key in existing_user:
    #         if key in updated_user_dict:
    #             setattr(user, key, updated_user_dict[key])

    #     db.add(user)
    #     db.commit()
    #     db.refresh(user)

    #     return user
    
    @staticmethod
    def partially_update_user(db: Session, user_id: str, data: UserPatch):

        # Get the book by id
        user = User_Crud.get_user_by_id(db, user_id)
        # user = db.query(User).filter(User.id == user_id).first()

        if not user:
            return None
        
        # Convert to dict
        new_user_dict = data.model_dump(exclude_unset=True)

        # Update the user in the database
        for key, value in new_user_dict.items():
            setattr(user, key, value)

        db.add(user)
        db.commit()
        db.refresh(user)

        return user
    

    @staticmethod
    def delete_user(db:Session, user_id: str):
        user = User_Crud.get_user_by_id(db, user_id)

        if not user:
            return None
        
        db.delete(user)
        db.commit()
        
        return {"message": "User deleted successfully"}
       
    
User_Crud = UserCrud()
