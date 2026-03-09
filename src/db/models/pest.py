from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from db.base import Base  

class Pest(Base):
    __tablename__ = "pests"

    id: Mapped[int]   = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)

    def __repr__(self):
        return f"<Pest(id={self.id}, name='{self.name}')>"
