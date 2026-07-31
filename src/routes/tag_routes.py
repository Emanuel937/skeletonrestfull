from fastapi import APIRouter, Depends
from model.base import get_session
from services.tag_service import TagService
from schemas.tag_schemas import TagCreate, TagUpdate

router = APIRouter(prefix="/tags", tags=["Tags"])
service = TagService()

@router.post("/")
def create_tag(data: TagCreate, db = Depends(get_session)):
    return service.create(data, db=db)

@router.get("/")
def list_tags(db = Depends(get_session)):
    return service.list(db=db)

@router.get("/{id}")
def get_tag(id: int, db = Depends(get_session)):
    return service.get(id, db=db)

@router.put("/{id}")
def update_tag(id: int, data: TagUpdate, db = Depends(get_session)):
    return service.update(id, data, db=db)

@router.delete("/{id}")
def delete_tag(id: int, db = Depends(get_session)):
    return service.delete(id, db=db)
