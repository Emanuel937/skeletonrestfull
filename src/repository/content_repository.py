from model.content_modal import Content
from repository.base_repository import BaseRepository

# ContentRepository manages all content types (lesson, exercise, audio...)
# Inherits:
# - create()
# - get_by_id()
# - list_all()
# - update()
# - delete()
class ContentRepository(BaseRepository):
    def __init__(self):
        super().__init__(Content)

    # Custom method
    def list_by_type(self, type_name: str, db):
        return db.query(Content).filter(Content.type == type_name).all()
