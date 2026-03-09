from sqlalchemy import Column, Integer, String
from db.base import Base      


class UserProducts(Base):
    __tablename__ = "user_products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    company_id = Column(Integer, nullable=False)
    product_name = Column(String(255), nullable=False)
    product_description = Column(String(255), nullable=True)
    product_reference = Column(String(255), nullable=True)
    product_composition = Column(String(255), nullable=True)
    product_unite  = Column(String(50), nullable=True)
    product_qlt = Column(String(50), nullable=True)

    def __repr__(self):
        return f"<UserProducts(id={self.id}, user_id={self.user_id}, product_id={self.product_id})>"