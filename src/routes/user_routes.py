from fastapi import APIRouter, Depends
from model.base import get_session
from services.users_service import UserService
from schemas.users_schema import UserCreate, UserUpdate

router = APIRouter(prefix="/users", tags=["Users"])
service = UserService()

@router.post("/")
def create_user(data: UserCreate, db = Depends(get_session)):
    return service.create(data, db=db)

@router.get("/")
def list_users(db = Depends(get_session)):
    return service.list(db=db)

@router.get("/{id}")
def get_user(id: int, db = Depends(get_session)):
    return service.get(id, db=db)

@router.put("/{id}")
def update_user(id: int, data: UserUpdate, db = Depends(get_session)):
    return service.update(id, data, db=db)

@router.delete("/{id}")
def delete_user(id: int, db = Depends(get_session)):
    return service.delete(id, db=db)
