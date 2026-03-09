from sqlalchemy import Column, Integer, String
from db.base import Base

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    phone_number = Column(String(20), nullable=True)

    def __repr__(self):
        return f"<Client(id={self.id}, name='{self.name}', email='{self.email}')>"
