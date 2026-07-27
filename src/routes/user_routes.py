from fastapi import APIRouter
from services.users_service import UserService
from schemas.users_schema import UserCreate, UserUpdate

router = APIRouter(prefix="/users", tags=["Users"])
service = UserService()

@router.post("/")
def create_user(data: UserCreate):
    return service.create(data)

@router.get("/")
def list_users():
    return service.list()

@router.get("/{id}")
def get_user(id: int):
    return service.get(id)

@router.put("/{id}")
def update_user(id: int, data: UserUpdate):
    return service.update(id, data)

@router.delete("/{id}")
def delete_user(id: int):
    return service.delete(id)
