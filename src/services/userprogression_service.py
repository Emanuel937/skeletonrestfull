from fastapi import HTTPException

from services.base_service import BaseService
from repository.userprogression_repository import UserProgressRepository

class UserProgressService(BaseService):
    def __init__(self):
        super().__init__(UserProgressRepository())

    def get_progress(self, user_id: int, content_id: int):
        progress = self.crud.get_progress(user_id, content_id)
        if not progress:
            raise HTTPException(status_code=404, detail="Progress not found")
        return progress

    def list_for_user(self, user_id: int):
        return self.crud.list_user_progress(user_id)
