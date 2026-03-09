from sqlalchemy import Integer, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.base import Base

class Capture(Base):
    
    """
    Stores the number of pests captured in a specific area on a given date.
    This table is the foundation for monthly trend analysis (e.g., 22 rodents exterior in January).
    """

    __tablename__ = "captures"

    id:       Mapped[int]  = mapped_column(Integer, primary_key=True, autoincrement=True)
    date:     Mapped[Date] = mapped_column(Date, nullable=False)
    area_id:  Mapped[int]  = mapped_column(ForeignKey("areas.id"), nullable=False)
    pest_id:  Mapped[int]  = mapped_column(ForeignKey("pests.id"), nullable=False)
    quantity: Mapped[int]  = mapped_column(Integer, nullable=True)
    area = relationship("Area")
    pest = relationship("Pest")

    def __repr__(self):
        return f"<Capture(id={self.id}, date={self.date}, quantity={self.quantity})>"
