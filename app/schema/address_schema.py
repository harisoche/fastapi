from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class AddressBaseSchema(BaseModel):
    user_id: Optional[int] = None
    address: str
    city: str
    province: str
    country: str
    postal_code: str
    is_primary: bool

    class Config:
        orm_mode = True


class AddressUpdateSchema(AddressBaseSchema):
    id: int
    user_id: int
    address: Optional[str] = None
    city: Optional[str] = None
    province: Optional[str] = None
    country: Optional[str] = None
    postal_code: Optional[str] = None
    is_primary: Optional[bool] = False


class AddressResponseSchema(AddressBaseSchema):
    id: int
    created_at: datetime
    updated_at: datetime