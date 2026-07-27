from fastapi import APIRouter
from services.tag_service import TagService
from schemas.tag_schemas import TagCreate, TagUpdate

router = APIRouter(prefix="/tags", tags=["Tags"])
service = TagService()

@router.post("/")
def create_tag(data: TagCreate):
    return service.create(data)

@router.get("/")
def list_tags():
    return service.list()

@router.get("/{id}")
def get_tag(id: int):
    return service.get(id)

@router.put("/{id}")
def update_tag(id: int, data: TagUpdate):
    return service.update(id, data)

@router.delete("/{id}")
def delete_tag(id: int):
    return service.delete(id)
