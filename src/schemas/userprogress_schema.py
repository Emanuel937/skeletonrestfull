from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# UserProgress tracks how each user interacts with specific Content items.
# It is inspired by WordPress "wp_usermeta", but structured cleanly.
#
# This table allows storing:
# - the user's score for an exercise or lesson
# - whether the content has been completed
# - the last time the user interacted with the content
#
# This enables features such as:
# - learning progression tracking
# - personalized recommendations
# - resume where you left off
# - statistics and performance analytics
#
# Each row represents one user's progress on one content item.
class UserProgressCreate(BaseModel):
    user_id: int
    content_id: int
    score: Optional[int] = 0
    completed: Optional[bool] = False


class UserProgressUpdate(BaseModel):
    score: Optional[int] = None
    completed: Optional[bool] = None

    class Config:
        orm_mode = True


class UserProgressResponse(BaseModel):
    id: int
    user_id: int
    content_id: int
    score: int
    completed: bool
    last_seen: datetime

    class Config:
        from_attributes = True
