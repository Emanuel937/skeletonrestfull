from services.base_service import BaseService
from repository.content_repository import ContentRepository

class ContentService(BaseService):
    def __init__(self):
        super().__init__(ContentRepository())
