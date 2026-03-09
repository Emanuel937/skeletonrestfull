from db.base import SessionLocal
from db.models import User
from sqlalchemy.exc import NoResultFound

class UserCRUD:
    def __init__(self):
        self.db = SessionLocal()

    def create_user(self, username: str, email: str, password: str, company_id: int = None) -> User:
        new_user = User(username=username, email=email, password=password, company_id=company_id)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

    def get_user_by_id(self, user_id: int) -> User:
        try:
            user = self.db.query(User).filter(User.id == user_id).one()
            return user
        except NoResultFound:
            return None

    def get_user_by_email(self, email: str) -> User:
        try:
            user = self.db.query(User).filter(User.email == email).one()
            return user
        except NoResultFound:
            return None

    def update_user(self, user_id: int, **kwargs) -> User:
        user = self.get_user_by_id(user_id)
        if not user:
            return None
        for key, value in kwargs.items():
            setattr(user, key, value)
        self.db.commit()
        self.db.refresh(user)
        return user

    def delete_user(self, user_id: int) -> bool:
        user = self.get_user_by_id(user_id)
        if not user:
            return False
        self.db.delete(user)
        self.db.commit()
        return True