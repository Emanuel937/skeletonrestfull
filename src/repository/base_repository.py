from model.base import SessionLocal
from sqlalchemy.exc import NoResultFound

# BaseRepository provides generic CRUD operations for any SQLAlchemy model.
# It centralizes common database logic so individual repositories remain simple.
#
# Features:
# - create(**kwargs)       → insert a new row
# - get_by_id(id)          → fetch one row by primary key
# - list_all()             → return all rows
# - update(id, **kwargs)   → update fields dynamically
# - delete(id)             → remove a row
#
# Usage:
#   TagRepository(BaseRepository)
#   ContentRepository(BaseRepository)
#   UserRepository(BaseRepository)
#
# This pattern avoids repeating CRUD code and keeps your project clean and scalable.
class BaseRepository:
    def __init__(self, model):
        self.db = SessionLocal()
        self.model = model

    def create(self, **kwargs):
        obj = self.model(**kwargs)
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def get_by_id(self, obj_id: int):
        try:
            return self.db.query(self.model).filter(self.model.id == obj_id).one()
        except NoResultFound:
            return None

    def list_all(self):
        return self.db.query(self.model).all()

    def update(self, obj_id: int, **kwargs):
        obj = self.get_by_id(obj_id)
        if not obj:
            return None
        for key, value in kwargs.items():
            setattr(obj, key, value)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def delete(self, obj_id: int):
        obj = self.get_by_id(obj_id)
        if not obj:
            return False
        self.db.delete(obj)
        self.db.commit()
        return True
