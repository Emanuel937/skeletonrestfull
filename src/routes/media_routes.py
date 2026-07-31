from fastapi import APIRouter, UploadFile, File, Form, Depends
from model.base import get_session
from services.media_service import MediaAssetService
from schemas.media_schemas import MediaAssetCreate, MediaAssetUpdate
from utils.upload import save_media_file
from typing import List

router = APIRouter(prefix="/media", tags=["Media"])
service = MediaAssetService()

# -----------------------------
# CREATE (with file upload)
# -----------------------------
@router.post("/")
async def create_media(
    file: UploadFile = File(...),
    name: str = Form(...),
    type: str = Form(...),
    size: str = Form(...),
    altText: str = Form(...),
    dimensions: str = Form(...),
    linkedTagIds: List[str] = Form([]),
    linkedContentIds: List[str] = Form([]),
    db = Depends(get_session)
):
    # Save file to disk
    file_location = save_media_file(file=file)
    
    # Build payload for your service
    payload = MediaAssetCreate(
        name=name,
        url=file_location,
        type=type,
        size=size,
        dimensions=dimensions,
        altText=altText,
        linkedTagIds=linkedTagIds,
        linkedContentIds=linkedContentIds,
    )
    return service.create(payload, db=db)

# -----------------------------
# LIST ALL
# -----------------------------
@router.get("/")
def list_media(db = Depends(get_session)):
    return service.list(db=db)

# -----------------------------
# GET ONE
# -----------------------------
@router.get("/{id}")
def get_media(id: str, db = Depends(get_session)):
    return service.get(id, db=db)

# -----------------------------
# UPDATE
# -----------------------------
@router.put("/{id}")
def update_media(id: str, data: MediaAssetUpdate, db = Depends(get_session)):
    return service.update(id, data, db=db)

# -----------------------------
# DELETE
# -----------------------------
@router.delete("/{id}")
def delete_media(id: str, db = Depends(get_session)):
    return service.delete(id, db=db)
