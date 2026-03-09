from db.base import SessionLocal
from db.models.areas import Area
from sqlalchemy.exc import NoResultFound


class AreaCRUD:
    def __init__(self):
        self.db = SessionLocal()

    def create_area(self, name: str) -> Area:
        new_area = Area(name=name)
        self.db.add(new_area)
        self.db.commit()
        self.db.refresh(new_area)
        return new_area

    def get_area_by_id(self, area_id: int) -> Area:
        try:
            return self.db.query(Area).filter(Area.id == area_id).one()
        except NoResultFound:
            return None

    def get_area_by_name(self, name: str) -> Area:
        try:
            return self.db.query(Area).filter(Area.name == name).one()
        except NoResultFound:
            return None

    def list_areas(self) -> list[Area]:
        return self.db.query(Area).all()

    def update_area(self, area_id: int, **kwargs) -> Area:
        area = self.get_area_by_id(area_id)
        if not area:
            return None
        for key, value in kwargs.items():
            setattr(area, key, value)
        self.db.commit()
        self.db.refresh(area)
        return area

    def delete_area(self, area_id: int) -> bool:
        area = self.get_area_by_id(area_id)
        if not area:
            return False
        self.db.delete(area)
        self.db.commit()
        return True
