from sqlalchemy import String, ForeignKey, Integer, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from db.base import Base



# ----------------------
# User Table
# ----------------------
class User(Base):
    __tablename__ = "users"

    id: Mapped[int]                = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str]          = mapped_column(String(255), unique=True, nullable=False)
    email: Mapped[str]             = mapped_column(String(255), unique=True, nullable=False)
    password: Mapped[str]          = mapped_column(String(255), nullable=False)
    company_id: Mapped[int]        = mapped_column(ForeignKey("companies.id"), nullable=True)
    is_active: Mapped[bool]        = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime]   = mapped_column(DateTime, default=datetime.utcnow)

    company: Mapped["Company"]     =  relationship("Company", back_populates="users")
    roles: Mapped[list["Role"]]    = relationship(
        "Role", secondary="user_roles", back_populates="users"
    )

    def __repr__(self):
        return f"<User id={self.id} username={self.username} email={self.email}>"
