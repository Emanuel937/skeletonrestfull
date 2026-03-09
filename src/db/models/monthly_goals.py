from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.base import Base

class MonthlyGoal(Base):
    
    __tablename__ = "monthly_goals"

    id: Mapped[int]      = mapped_column(Integer, primary_key=True, autoincrement=True)
    pest_id: Mapped[int] = mapped_column(ForeignKey("pests.id"), nullable=False)
    area_id: Mapped[int] = mapped_column(ForeignKey("areas.id"), nullable=True)
    month: Mapped[int]   = mapped_column(Integer, nullable=False)
    year: Mapped[int]    = mapped_column(Integer, nullable=False)
    goal: Mapped[str]    = mapped_column(String(255), nullable=False)
    priority: Mapped[str] = mapped_column(String(50), nullable=True)
    pest = relationship("Pest")
    area = relationship("Area")

    def __repr__(self):
        return f"<MonthlyGoal(id={self.id}, month={self.month}, year={self.year})>"
