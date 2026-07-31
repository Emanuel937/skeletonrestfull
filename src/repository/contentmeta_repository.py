from model.contentmeta_modal import ContentMeta
from repository.base_repository import BaseRepository

# ContentMetaRepository manages metadata for content items.
# Inherits:
# - create()
# - get_by_id()
# - list_all()
# - update()
# - delete()
class ContentMetaRepository(BaseRepository):
    def __init__(self):
        super().__init__(ContentMeta)

    # Custom methods
    def get_meta(self, content_id: int, key: str):
        return (
            self.db.query(ContentMeta)
            .filter(ContentMeta.content_id == content_id, ContentMeta.key == key)
            .first()
        )

    def list_meta(self, content_id: int, db):
        return db.query(ContentMeta).filter(ContentMeta.content_id == content_id).all()
