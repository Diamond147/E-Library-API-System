from fastapi import HTTPException, status
from schemas.user import Deactivate
from sqlalchemy.orm import Session
from model import User


class UserService:
    
    @staticmethod
    def deactivate(db: Session, user_id: str, data: Deactivate):
        user = db.query(User).filter(User.id == user_id).first()

        if not user:
            return None
        
        Updated_status = data.model_dump(exclude_unset=True)

        for key, value in Updated_status.items():
            setattr(user, key, value)

        db.add(user)
        db.commit()
        db.refresh(user)

        return user