from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class UserBaseSchema(BaseModel):
    full_name: str
    username: str
    email: str
    password: str
    role_id: int

    class Config:
        orm_mode = True


class UserUpdateSchema(BaseModel):
    id: int
    full_name: Optional[str] = None
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    role_id: Optional[int] = None

    class Config:
        orm_mode = True


class UserResponseSchema(UserBaseSchema):
    id: int
    token: Optional[str] = None
    is_active: bool
    is_verified: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True