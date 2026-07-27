from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column
from model.base import Base

class ContentTag(Base):
    __tablename__ = "content_tags"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    content_id: Mapped[int] = mapped_column(Integer, nullable=False)
    tag_id: Mapped[int] = mapped_column(Integer, nullable=False)

    def __repr__(self):
        return f"<ContentTag id={self.id} content_id={self.content_id} tag_id={self.tag_id}>"
