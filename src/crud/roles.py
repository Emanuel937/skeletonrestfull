from db.base import SessionLocal
from db.models import Role

class RoleCRUD:
    def __init__(self):
        self.db = SessionLocal()
   
    def create_role(self, name: str, description: str = None) -> Role:
        new_role = Role(name=name, description=description)
        self.db.add(new_role)
        self.db.commit()
        self.db.refresh(new_role)
        return new_role

    def get_role_by_id(self, role_id: int) -> Role:
        return self.db.query(Role).filter(Role.id == role_id).first()

    def get_role_by_name(self, name: str) -> Role:
        return self.db.query(Role).filter(Role.name == name).first()

    def update_role(self, role_id: int, **kwargs) -> Role:
        role = self.get_role_by_id(role_id)
        if not role:
            return None
        for key, value in kwargs.items():
            setattr(role, key, value)
        self.db.commit()
        self.db.refresh(role)
        return role

    def delete_role(self, role_id: int) -> bool:
        role = self.get_role_by_id(role_id)
        if not role:
            return False
        self.db.delete(role)
        self.db.commit()
        return True