from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from model.base import Base

class ContentMeta(Base):
    __tablename__ = "content_meta"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    content_id: Mapped[int] = mapped_column(Integer, nullable=False)
    key: Mapped[str] = mapped_column(String(255), nullable=False)
    value: Mapped[str] = mapped_column(String, nullable=False)

    def __repr__(self):
        return f"<ContentMeta id={self.id} key={self.key}>"
