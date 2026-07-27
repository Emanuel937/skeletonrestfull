from pydantic import BaseModel
from typing import Optional

# ContentMeta stores any additional information (metadata) related to a Content item.
# It works like WordPress "wp_postmeta" and allows unlimited custom fields without
# modifying the database structure.
#
# Examples of metadata:
# - "difficulty"      → A1, B2, C1
# - "audio_url"       → path to TTS-generated audio
# - "correct_answer"  → expected answer for an exercise
# - "choices"         → JSON list of possible answers
# - "duration"        → estimated time to complete
#
# This makes the system extremely flexible: you can extend Content with any custom
# attributes simply by adding new key/value pairs.
class ContentMetaCreate(BaseModel):
    content_id: int
    key: str
    value: str


class ContentMetaUpdate(BaseModel):
    key: Optional[str] = None
    value: Optional[str] = None

    class Config:
        orm_mode = True


class ContentMetaResponse(BaseModel):
    id: int
    content_id: int
    key: str
    value: str

    class Config:
        from_attributes = True
