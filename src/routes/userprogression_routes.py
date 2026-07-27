from fastapi import APIRouter
from services.userprogression_service import UserProgressService
from schemas.userprogress_schema import UserProgressCreate, UserProgressUpdate

router = APIRouter(prefix="/user-progress", tags=["UserProgress"])
service = UserProgressService()

@router.post("/")
def create_progress(data: UserProgressCreate):
    return service.create(data)

@router.get("/")
def list_progress():
    return service.list()

@router.get("/{id}")
def get_progress(id: int):
    return service.get(id)

@router.put("/{id}")
def update_progress(id: int, data: UserProgressUpdate):
    return service.update(id, data)

@router.delete("/{id}")
def delete_progress(id: int):
    return service.delete(id)
