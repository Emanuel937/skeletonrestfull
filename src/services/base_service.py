from fastapi import HTTPException

class BaseService:
    def __init__(self, repository):
        self.crud = repository

    def create(self, data):
        obj_data = data.dict(exclude_unset=True)
        allowed_fields = set(self.crud.model.__table__.columns.keys())
        dynamic_data = {k: v for k, v in obj_data.items() if k in allowed_fields}

        return self.crud.create(**dynamic_data)

    def get(self, obj_id: int):
        obj = self.crud.get_by_id(obj_id)
        if not obj:
            raise HTTPException(status_code=404, detail="Not found")
        return obj

    def list(self):
        return self.crud.list_all()

    def update(self, obj_id: int, data):
        obj = self.crud.get_by_id(obj_id)
        if not obj:
            raise HTTPException(status_code=404, detail="Not found")

        update_data = data.dict(exclude_unset=True)
        allowed_fields = set(obj.__table__.columns.keys())

        dynamic_update = {k: v for k, v in update_data.items() if k in allowed_fields}

        updated = self.crud.update(obj_id, **dynamic_update)
        return updated

    def delete(self, obj_id: int):
        if not self.crud.delete(obj_id):
            raise HTTPException(status_code=404, detail="Not found")
        return {"detail": "Deleted"}