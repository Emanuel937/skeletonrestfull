from model.media_modal import MediaAsset
from repository.base_repository import BaseRepository


class MediaAssetRepository(BaseRepository):
    def __init__(self):
        super().__init__(MediaAsset)

    # Custom: list all media by type (image, video, audio...)
    def list_by_type(self, media_type: str, db):
        return db.query(MediaAsset).filter(MediaAsset.type == media_type).all()

    # Custom: find all media linked to a specific content ID
    def list_by_content(self, content_id: str, db):
        return (
            db.query(MediaAsset)
            .filter(MediaAsset.linkedContentIds.contains([content_id]))
            .all()
        )

    # Custom: find all media linked to a specific tag ID
    def list_by_tag(self, tag_id: str, db):
        return (
            db.query(MediaAsset)
            .filter(MediaAsset.linkedTagIds.contains([tag_id]))
            .all()
        )
