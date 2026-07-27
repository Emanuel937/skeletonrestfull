from services.base_service import BaseService
from repository.contentmeta_repository import ContentMetaRepository

class ContentMetaService(BaseService):
    def __init__(self):
        super().__init__(ContentMetaRepository())

    def list_for_content(self, content_id: int):
        return self.crud.list_meta(content_id)
