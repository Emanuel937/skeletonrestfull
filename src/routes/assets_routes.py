from fastapi import APIRouter
from fastapi.responses import FileResponse
from services.media_service import MediaAssetService


router = APIRouter(prefix="/uploads", tags=["uploads"])
service = MediaAssetService()

#---------------------------
# GET FILE
# -------------------------
@router.get("/media/{filename}")
async def get_media(filename: str):
    file_path = f"uploads/media/{filename}"
    return FileResponse(file_path)
