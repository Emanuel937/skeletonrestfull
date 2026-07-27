from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Tag represents any classification element used to organize Content.
# It is inspired by WordPress "wp_terms" and replaces multiple tables such as:
# - categories (Vocabulary, Grammar, Listening…)
# - levels (Beginner, Intermediate, Advanced)
# - topics (Travel, Business, Daily Life)
# - exercise types (Multiple Choice, Listening, Speaking)
#
# The "type" field defines what kind of taxonomy the tag belongs to:
# - type="category" → main content categories
# - type="level"    → difficulty levels
# - type="topic"    → thematic grouping
# - type="kind"     → exercise type or content subtype
#
# This makes the system extremely flexible: you can create unlimited taxonomies
# without adding new database tables.
class TagCreate(BaseModel):
    name: str
    slug: str
    type: Optional[str] = None


class TagUpdate(BaseModel):
    name: Optional[str] = None
    slug: Optional[str] = None
    type: Optional[str] = None

    class Config:
        orm_mode = True


class TagResponse(BaseModel):
    id: int
    name: str
    slug: str
    type: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True
