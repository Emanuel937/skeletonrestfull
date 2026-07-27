from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# User represents an authenticated account in the system.
# It stores essential identity information such as email and password.
#
# This model is intentionally minimal:
# - "email"        → unique identifier for login
# - "password"     → raw password received from the client (will be hashed before storage)
#
# Additional user-related data (preferences, settings, progress, roles, etc.)
# should NOT be added here. Instead, they are stored in dedicated tables such as:
# - UserProgress     → learning progression
# - ContentMeta      → custom metadata if needed
#
# This keeps the User table clean, secure, and easy to maintain.
class UserCreate(BaseModel):
    email: str
    password: str


class UserUpdate(BaseModel):
    email: Optional[str] = None
    password: Optional[str] = None

    class Config:
        orm_mode = True


class UserResponse(BaseModel):
    id: int
    email: str
    created_at: datetime

    class Config:
        from_attributes = True
