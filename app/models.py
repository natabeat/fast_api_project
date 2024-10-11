from pydantic import BaseModel
from typing import List

class User(BaseModel):
    id: int
    name: str
    liked_items: List[int]

class Item(BaseModel):
    id: int
    name: str
    description: str
    tags: List[str]
