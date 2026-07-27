from model.userprogression_modal import UserProgress
from repository.base_repository import BaseRepository

# UserProgressRepository tracks learning progression for each user.
# Inherits:
# - create()
# - get_by_id()
# - list_all()
# - update()
# - delete()
class UserProgressRepository(BaseRepository):
    def __init__(self):
        super().__init__(UserProgress)

    # Custom methods
    def get_progress(self, user_id: int, content_id: int):
        return (
            self.db.query(UserProgress)
            .filter(UserProgress.user_id == user_id, UserProgress.content_id == content_id)
            .first()
        )

    def list_user_progress(self, user_id: int):
        return self.db.query(UserProgress).filter(UserProgress.user_id == user_id).all()
