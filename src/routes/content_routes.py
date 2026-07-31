from fastapi import APIRouter, Depends
from model.base import get_session
from services.content_service import ContentService
from schemas.content_schemas import ContentCreate, ContentUpdate

router = APIRouter(prefix="/content", tags=["Content"])
service = ContentService()

@router.post("/")
def create_content(data: ContentCreate, db = Depends(get_session)):
    return service.create(data, db=db)

@router.get("/")
def list_content(db = Depends(get_session)):
    return service.list(db=db)

@router.get("/{id}")
def get_content(id: int, db = Depends(get_session)):
    return service.get(id, db=db)

@router.put("/{id}")
def update_content(id: int, data: ContentUpdate, db = Depends(get_session)):
    return service.update(id, data, db=db)

@router.delete("/{id}")
def delete_content(id: int, db = Depends(get_session)):
    return service.delete(id, db=db)
