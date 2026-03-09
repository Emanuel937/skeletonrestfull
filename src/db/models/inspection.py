from sqlalchemy import Integer, Date, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.base import Base


class Inspection(Base):
    """
    Stores inspection or operational actions performed in a specific area.
    Examples:
    - '126 traps inspected'
    - 'Night inspection 21h–02h'
    - 'Sealing of critical access points'
    - 'Installation of 4 mosquito control devices'
    """

    __tablename__ = "inspections"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    # Date when the inspection or action was performed
    date: Mapped[Date] = mapped_column(Date, nullable=False)

    # Area where the inspection took place
    area_id: Mapped[int] = mapped_column(ForeignKey("areas.id"), nullable=True)

    # Description of the action performed
    notes: Mapped[str] = mapped_column(Text, nullable=True)

    # ORM relationship
    area = relationship("Area")

    def __repr__(self):
        return f"<Inspection(id={self.id}, date={self.date})>"
