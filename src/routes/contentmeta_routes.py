from fastapi import APIRouter, Depends
from model.base import get_session
from services.contentmeta_service import ContentMetaService
from schemas.contentmeta_schema import ContentMetaCreate, ContentMetaUpdate

router = APIRouter(prefix="/content-meta", tags=["ContentMeta"])
service = ContentMetaService()

@router.post("/")
def create_meta(data: ContentMetaCreate, db = Depends(get_session)):
    return service.create(data, db=db)

@router.get("/")
def list_meta(db = Depends(get_session)):
    return service.list(db=db)

@router.get("/{id}")
def get_meta(id: int, db = Depends(get_session)):
    return service.get(id, db=db)

@router.put("/{id}")
def update_meta(id: int, data: ContentMetaUpdate, db = Depends(get_session)):
    return service.update(id, data, db=db)

@router.delete("/{id}")
def delete_meta(id: int, db = Depends(get_session)):
    return service.delete(id, db=db)
