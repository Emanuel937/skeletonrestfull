from fastapi import HTTPException
from repository.users_repository import UserRepository
from schemas.users_schema import UserCreate, UserUpdate
from passlib.context import CryptContext
from services.base_service import BaseService

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserService(BaseService):
    def __init__(self):
        super().__init__(UserRepository())

    def hash_password(self, password: str):
        return pwd_context.hash(password)

    def verify_password(self, plain: str, hashed: str):
        return pwd_context.verify(plain, hashed)

    def create(self, data: UserCreate):
        # Check email uniqueness
        if self.crud.get_by_email(data.email):
            raise HTTPException(status_code=400, detail="Email already exists")

        user_data = data.dict(exclude_unset=True)
        allowed_fields = set(self.crud.model.__table__.columns.keys())

        dynamic_data = {
            k: (self.hash_password(v) if k == "password_hash" else v)
            for k, v in user_data.items()
            if k in allowed_fields
        }

        return self.crud.create(**dynamic_data)

    def update(self, user_id: int, data: UserUpdate):
        user = self.get(user_id)

        update_data = data.dict(exclude_unset=True)
        allowed_fields = set(user.__table__.columns.keys())

        dynamic_update = {
            k: (self.hash_password(v) if k == "password_hash" else v)
            for k, v in update_data.items()
            if k in allowed_fields
        }

        return self.crud.update(user_id, **dynamic_update)
