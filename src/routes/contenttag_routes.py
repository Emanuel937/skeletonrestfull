from fastapi import APIRouter, Depends
from model.base import get_session
from services.contenttag_service import ContentTagService
from schemas.contenttag_schemas import ContentTagCreate, ContentTagUpdate

router = APIRouter(prefix="/content-tags", tags=["ContentTags"])
service = ContentTagService()

@router.post("/")
def create_content_tag(data: ContentTagCreate, db = Depends(get_session)):
    return service.create(data, db=db)

@router.get("/")
def list_content_tags(db = Depends(get_session)):
    return service.list(db=db)

@router.get("/{id}")
def get_content_tag(id: int, db = Depends(get_session)):
    return service.get(id, db=db)

@router.put("/{id}")
def update_content_tag(id: int, data: ContentTagUpdate, db = Depends(get_session)):
    return service.update(id, data, db=db)

@router.delete("/{id}")
def delete_content_tag(id: int, db = Depends(get_session)):
    return service.delete(id, db=db)
