from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from enum import Enum


class MediaType(str, Enum):
    image = "image"
    video = "video"
    audio = "audio"
    document = "document"
    other = "other"


# -----------------------------
# CREATE
# -----------------------------
class MediaAssetCreate(BaseModel):
    name: str
    url: str
    type: MediaType
    size: str
    dimensions: Optional[str] = None
    caption: Optional[str] = None
    altText: Optional[str] = None
    linkedContentIds: List[str] = []
    linkedTagIds: List[str] = []


# -----------------------------
# UPDATE
# -----------------------------
class MediaAssetUpdate(BaseModel):
    name: Optional[str] = None
    url: Optional[str] = None
    type: Optional[MediaType] = None
    size: Optional[str] = None
    dimensions: Optional[str] = None
    caption: Optional[str] = None
    altText: Optional[str] = None
    linkedContentIds: Optional[List[str]] = None
    linkedTagIds: Optional[List[str]] = None

    class Config:
        orm_mode = True


# -----------------------------
# RESPONSE
# -----------------------------
class MediaAssetResponse(BaseModel):
    id: str
    name: str
    url: str
    type: MediaType
    size: str
    dimensions: Optional[str]
    caption: Optional[str]
    altText: Optional[str]
    linkedContentIds: List[str]
    linkedTagIds: List[str]
    created_at: datetime

    class Config:
        from_attributes = True
