from fastapi import HTTPException

class BaseService:
    def __init__(self, repository):
        self.crud = repository

    def create(self, data, db):
        obj_data = data.dict(exclude_unset=True)
        allowed_fields = set(self.crud.model.__table__.columns.keys())
        dynamic_data = {k: v for k, v in obj_data.items() if k in allowed_fields}
        return self.crud.create(db, **dynamic_data)

    def get(self, obj_id: int, db):
        obj = self.crud.get_by_id(db, obj_id)
        if not obj:
            raise HTTPException(status_code=404, detail="Not found")
        return obj

    def list(self, db):
        return self.crud.list_all(db)

    def update(self, obj_id: int, data, db):
        obj = self.crud.get_by_id(db, obj_id)
        if not obj:
            raise HTTPException(status_code=404, detail="Not found")

        update_data = data.dict(exclude_unset=True)
        allowed_fields = set(obj.__table__.columns.keys())
        dynamic_update = {k: v for k, v in update_data.items() if k in allowed_fields}

        return self.crud.update(db, obj_id, **dynamic_update)

    def delete(self, obj_id: int, db):
        if not self.crud.delete(db, obj_id):
            raise HTTPException(status_code=404, detail="Not found")
        return {"detail": "Deleted"}
