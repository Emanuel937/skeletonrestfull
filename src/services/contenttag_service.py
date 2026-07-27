from services.base_service import BaseService
from repository.contenttag_repository import ContentTagRepository

class ContentTagService(BaseService):
    def __init__(self):
        super().__init__(ContentTagRepository())

    def tags_for_content(self, content_id: int):
        return self.crud.list_tags_for_content(content_id)

    def content_for_tag(self, tag_id: int):
        return self.crud.list_content_for_tag(tag_id)
