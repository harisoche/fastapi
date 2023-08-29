from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy import false
from sqlalchemy import select, update, delete
from app.database import Base, db
from datetime import datetime
from fastapi import HTTPException, status
from app.schema import AddressBaseSchema


class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    address = Column(String(255), nullable=False)
    city = Column(String(50), nullable=False)
    province = Column(String(50), nullable=False)
    country = Column(String(50), nullable=False)
    postal_code = Column(String(10), nullable=False)
    is_primary = Column(Boolean, nullable=False, default=false())
    created_at = Column(DateTime, nullable=False, server_default=datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))
    updated_at = Column(DateTime, nullable=False, server_default=datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))

    def __repr__(self):
        return f"<Address(address={self.address})>"

    @classmethod
    async def create(cls, obj: AddressBaseSchema):
        address = cls(**dict(obj))
        db.add(address)

        try:
            await db.commit()
        except:
            await db.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Address already exists")

        return address

    @classmethod
    async def get_by_id(cls, id: int):
        address = await db.execute(select(cls).where(cls.id == id))
        address = address.scalar_one_or_none()
        if address is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Address not found")

        return address

    @classmethod
    async def get_by_user_id(cls, user_id: int):
        address = await db.execute(select(cls).where(cls.user_id == user_id))
        address = address.scalars().all()
        if address is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Address not found")

        return address

    @classmethod
    async def update(cls, obj: dict):
        await db.execute(update(cls).where(cls.id == obj['id']).values(obj))
        try:
            await db.commit()
        except:
            await db.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")

        return obj

    @classmethod
    async def delete(cls, id: int):
        await db.execute(delete(cls).where(cls.id == id))
        try:
            await db.commit()
        except:
            await db.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")

        return True