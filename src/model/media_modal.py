from sqlalchemy import String, DateTime, Text, Enum, JSON, Integer
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from enum import Enum as PyEnum
from model.base import Base


class MediaType(str, PyEnum):
    image = "image"
    video = "video"
    audio = "audio"
    document = "document"
    other = "other"


class MediaAsset(Base):
    __tablename__ = "media_assets"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    url: Mapped[str] = mapped_column(String(500), nullable=False)
    type: Mapped[MediaType] = mapped_column(Enum(MediaType), nullable=False)

    size: Mapped[str] = mapped_column(String(50), nullable=False)
    dimensions: Mapped[str | None] = mapped_column(String(50), nullable=True)

    caption: Mapped[str | None] = mapped_column(Text, nullable=True)
    altText: Mapped[str | None] = mapped_column(Text, nullable=True)

    linkedContentIds: Mapped[list[str]] = mapped_column(JSON, default=[])
    linkedTagIds: Mapped[list[str]] = mapped_column(JSON, default=[])

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<MediaAsset id={self.id} name={self.name} type={self.type}>"
