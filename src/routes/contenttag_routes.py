from fastapi import APIRouter
from services.contenttag_service import ContentTagService
from schemas.contenttag_schemas import ContentTagCreate, ContentTagUpdate

router = APIRouter(prefix="/content-tags", tags=["ContentTags"])
service = ContentTagService()

@router.post("/")
def create_content_tag(data: ContentTagCreate):
    return service.create(data)

@router.get("/")
def list_content_tags():
    return service.list()

@router.get("/{id}")
def get_content_tag(id: int):
    return service.get(id)

@router.put("/{id}")
def update_content_tag(id: int, data: ContentTagUpdate):
    return service.update(id, data)

@router.delete("/{id}")
def delete_content_tag(id: int):
    return service.delete(id)
