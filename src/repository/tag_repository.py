from model.tag_model import Tag
from repository.base_repository import BaseRepository

# TagRepository manages taxonomy elements (categories, levels, topics...)
# Inherits:
# - create()
# - get_by_id()
# - list_all()
# - update()
# - delete()

class TagRepository(BaseRepository):
    def __init__(self):
        super().__init__(Tag)

    def get_by_slug(self, db, slug: str):
        return db.query(Tag).filter(Tag.slug == slug).first()
