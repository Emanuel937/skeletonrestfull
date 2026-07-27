from model.userprogression_modal import User
from repository.base_repository import BaseRepository

# UserRepository manages user accounts.
# Inherits:
# - create()
# - get_by_id()
# - list_all()
# - update()
# - delete()
class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__(User)

    # Custom method
    def get_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()
