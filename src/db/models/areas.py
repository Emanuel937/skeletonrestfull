from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from db.base import Base


class Area(Base):
    __tablename__ = "areas"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)

    def __repr__(self):
        return f"<Area(id={self.id}, name='{self.name}')>"