from sqlalchemy import String, Integer, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from db.base import Base

class Company(Base):

    __tablename__ = "companies"

    id: Mapped[int]                = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str]              = mapped_column(String(255), unique=True, nullable=False)
    created_at: Mapped[datetime]   = mapped_column(DateTime, default=datetime.utcnow)
    users: Mapped[list["User"]]    = relationship("User", back_populates="company")
    emails: Mapped[str]            = mapped_column(String(255), unique=True, nullable=False)
    address: Mapped[str]           = mapped_column(String(255), nullable=True)
    phone_number: Mapped[str]      = mapped_column(String(20), nullable=True)
    is_active: Mapped[bool]        = mapped_column(Boolean, default=True)
    logo_url: Mapped[str]          = mapped_column(String(255), nullable=True)
    
    def __repr__(self):
        return f"<Company(id={self.id}, name='{self.name}')>"