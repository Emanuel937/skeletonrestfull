from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.base import Base
from db.models.user import User      

class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=True)

    users: Mapped[list["User"]] = relationship(
        "User", secondary="user_roles", back_populates="roles"
    )

    def __repr__(self):
        return f"<Role id={self.id} name={self.name}>"
