from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Content class allows storing ANY type of content.
# The "type" field defines what the content represents:
# - "post"       → article, lesson, vocabulary item
# - "exercise"   → quiz, question, listening exercise
# - "audio"      → TTS-generated audio
# - "comment"    → user comment or feedback
# - "dialogue"   → conversation script
# - "note"       → user notes
# This structure is inspired by WordPress wp_posts and makes the DB extremely flexible.
class ContentCreate(BaseModel):
    type: str
    title: Optional[str] = None
    body: Optional[str] = None


class ContentUpdate(BaseModel):
    title: Optional[str] = None
    body: Optional[str] = None

    class Config:
        orm_mode = True


class ContentResponse(BaseModel):
    id: int
    type: str
    title: Optional[str]
    body: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True
