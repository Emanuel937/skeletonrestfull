from services.base_service import BaseService
from repository.tag_repository import TagRepository

class TagService(BaseService):
    def __init__(self):
        super().__init__(TagRepository())



