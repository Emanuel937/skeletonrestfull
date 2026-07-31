from model.contenttag_modal import ContentTag
from repository.base_repository import BaseRepository

# ContentTagRepository manages the many-to-many relationship between Content and Tag.
# Inherits:
# - create()
# - get_by_id()
# - list_all()
# - update()
# - delete()
class ContentTagRepository(BaseRepository):
    def __init__(self):
        super().__init__(ContentTag)

    # Custom methods
    def list_tags_for_content(self, content_id: int, db):
        return db.query(ContentTag).filter(ContentTag.content_id == content_id).all()

    def list_content_for_tag(self, tag_id: int, db):
        return db.query(ContentTag).filter(ContentTag.tag_id == tag_id).all()
