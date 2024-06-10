
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel,Field

class ItemStatus(Enum):
    NEW= 'new' 
    APPROVED='approved'
    EOL='eol'


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    owner_id: int
    status: ItemStatus = Field(default=ItemStatus.NEW)  # Explicit default with Field

    class Config:
        orm_mode = True

class UserId(BaseModel):
    id: int

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True