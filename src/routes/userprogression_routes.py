from fastapi import APIRouter, Depends
from model.base import get_session
from services.userprogression_service import UserProgressService
from schemas.userprogress_schema import UserProgressCreate, UserProgressUpdate

router = APIRouter(prefix="/user-progress", tags=["UserProgress"])
service = UserProgressService()

@router.post("/")
def create_progress(data: UserProgressCreate, db = Depends(get_session)):
    return service.create(data, db=db)

@router.get("/")
def list_progress(db = Depends(get_session)):
    return service.list(db=db)

@router.get("/{id}")
def get_progress(id: int, db = Depends(get_session)):
    return service.get(id, db=db)

@router.put("/{id}")
def update_progress(id: int, data: UserProgressUpdate, db = Depends(get_session)):
    return service.update(id, data, db=db)

@router.delete("/{id}")
def delete_progress(id: int, db = Depends(get_session)):
    return service.delete(id, db=db)
