# Code generated by sqlc. DO NOT EDIT.
# versions:
#   sqlc v1.15.0
import pydantic
from typing import Optional


class Author(pydantic.BaseModel):
    id: int
    name: str
    bio: Optional[str]