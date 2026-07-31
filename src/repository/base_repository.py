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
        self.model = model

    def create(self, db, **kwargs):
        obj = self.model(**kwargs)
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    def get_by_id(self, db, obj_id: int):
        try:
            return db.query(self.model).filter(self.model.id == obj_id).one()
        except NoResultFound:
            return None

    def list_all(self, db):
        return db.query(self.model).all()

    def update(self, db, obj_id: int, **kwargs):
        obj = self.get_by_id(db, obj_id)
        if not obj:
            return None
        for key, value in kwargs.items():
            setattr(obj, key, value)
        db.commit()
        db.refresh(obj)
        return obj

    def delete(self, db, obj_id: int):
        obj = self.get_by_id(db, obj_id)
        if not obj:
            return False
        db.delete(obj)
        db.commit()
        return True
