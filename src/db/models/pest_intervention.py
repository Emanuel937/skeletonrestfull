from sqlalchemy import Integer, String, TIME, Date, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.base import Base


class PestIntervention(Base):
    
    __tablename__ = "pest_interventions"

    id: Mapped[int]      = mapped_column(Integer, primary_key=True, autoincrement=True)
    date: Mapped[Date]   = mapped_column(Date, nullable=False)
    time: Mapped[TIME]   = mapped_column(TIME, nullable=True)
    product: Mapped[str] = mapped_column(String(255), nullable=True)
    registration_number: Mapped[str] = mapped_column(String(255), nullable=True)
    pest_id: Mapped[int] = mapped_column(ForeignKey("pests.id"), nullable=True)
    area_id: Mapped[int] = mapped_column(ForeignKey("areas.id"), nullable=True)
    pest = relationship("Pest")
    area = relationship("Area")
    method: Mapped[str] = mapped_column(String(255), nullable=True)
    dosage: Mapped[str] = mapped_column(String(255), nullable=True)
    quantity: Mapped[str] = mapped_column(String(255), nullable=True)
    notes: Mapped[str] = mapped_column(Text, nullable=True)

    def __repr__(self):
        return f"<PestIntervention(id={self.id}, date={self.date}, product='{self.product}')>"
