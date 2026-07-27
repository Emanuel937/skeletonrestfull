from fastapi import APIRouter
from services.content_service import ContentService
from schemas.content_schemas import ContentCreate, ContentUpdate

router = APIRouter(prefix="/content", tags=["Content"])
service = ContentService()

@router.post("/")
def create_content(data: ContentCreate):
    return service.create(data)

@router.get("/")
def list_content():
    return service.list()

@router.get("/{id}")
def get_content(id: int):
    return service.get(id)

@router.put("/{id}")
def update_content(id: int, data: ContentUpdate):
    return service.update(id, data)

@router.delete("/{id}")
def delete_content(id: int):
    return service.delete(id)
