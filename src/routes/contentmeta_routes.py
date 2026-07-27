from fastapi import APIRouter
from services.contentmeta_service import ContentMetaService
from schemas.contentmeta_schema import ContentMetaCreate, ContentMetaUpdate

router = APIRouter(prefix="/content-meta", tags=["ContentMeta"])
service = ContentMetaService()

@router.post("/")
def create_meta(data: ContentMetaCreate):
    return service.create(data)

@router.get("/")
def list_meta():
    return service.list()

@router.get("/{id}")
def get_meta(id: int):
    return service.get(id)

@router.put("/{id}")
def update_meta(id: int, data: ContentMetaUpdate):
    return service.update(id, data)

@router.delete("/{id}")
def delete_meta(id: int):
    return service.delete(id)
