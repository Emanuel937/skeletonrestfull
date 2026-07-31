from fastapi import APIRouter
from services.media_service import MediaAssetService

router = APIRouter(prefix="/testing", tags=["uploads"])
service = MediaAssetService()

#---------------------------
# GET FILE
# -------------------------
@router.get("/")
async def test():
    return {"status": "ok"}
