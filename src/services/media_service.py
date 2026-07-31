from fastapi import HTTPException
from repository.media_repository import MediaAssetRepository


class MediaAssetService:
    def __init__(self):
        self.crud = MediaAssetRepository()

    def create(self, data):
        obj_data = data.dict(exclude_unset=True)
        allowed_fields = set(self.crud.model.__table__.columns.keys())
        dynamic_data = {k: v for k, v in obj_data.items() if k in allowed_fields}

        return self.crud.create(**dynamic_data)

    def get(self, obj_id: str):
        obj = self.crud.get_by_id(obj_id)
        if not obj:
            raise HTTPException(status_code=404, detail="Media not found")
        return obj

    def list(self):
        return self.crud.list_all()

    def update(self, obj_id: str, data):
        obj = self.crud.get_by_id(obj_id)
        if not obj:
            raise HTTPException(status_code=404, detail="Media not found")

        update_data = data.dict(exclude_unset=True)
        allowed_fields = set(obj.__table__.columns.keys())
        dynamic_update = {k: v for k, v in update_data.items() if k in allowed_fields}

        updated = self.crud.update(obj_id, **dynamic_update)
        return updated

    def delete(self, obj_id: str):
        if not self.crud.delete(obj_id):
            raise HTTPException(status_code=404, detail="Media not found")
        return {"detail": "Deleted"}

    # Custom service methods
    def list_by_type(self, media_type: str):
        return self.crud.list_by_type(media_type)

    def list_by_content(self, content_id: str):
        return self.crud.list_by_content(content_id)

    def list_by_tag(self, tag_id: str):
        return self.crud.list_by_tag(tag_id)
