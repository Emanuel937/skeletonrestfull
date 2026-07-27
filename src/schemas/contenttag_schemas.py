from pydantic import BaseModel
from typing import Optional

# ContentTag is the link table that connects Content items to Tags.
# It represents a many‑to‑many relationship:
# - One Content can have multiple Tags (category, level, topic, type…)
# - One Tag can be assigned to multiple Content items
#
# This is the equivalent of WordPress "wp_term_relationships".
# It allows flexible classification without creating extra tables.
class ContentTagCreate(BaseModel):
    content_id: int
    tag_id: int


class ContentTagUpdate(BaseModel):
    content_id: Optional[int] = None
    tag_id: Optional[int] = None

    class Config:
        orm_mode = True


class ContentTagResponse(BaseModel):
    id: int
    content_id: int
    tag_id: int

    class Config:
        from_attributes = True
