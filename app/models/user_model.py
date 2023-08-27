from sqlalchemy import Column, Integer, String, DateTime, SmallInteger, Boolean
from sqlalchemy import false, true
from app.database import Base, db
from datetime import datetime
from sqlalchemy import select, update, delete, or_
from app.schema.user_schema import UserBaseSchema
from fastapi import HTTPException, status


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(60), nullable=False)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    token = Column(String(255), nullable=True)
    expired_at = Column(DateTime, nullable=True)
    role_id = Column(SmallInteger, nullable=False)
    is_active = Column(Boolean, nullable=False, default=true())
    is_verified = Column(Boolean, nullable=True, default=false())
    created_at = Column(DateTime, nullable=False, server_default=datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))
    updated_at = Column(DateTime, nullable=False, server_default=datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))

    def __repr__(self):
        return f"<User(fullName={self.full_name})>"

    @classmethod
    async def create(cls, obj: UserBaseSchema):
        # Create a user instance using the provided data from UserBaseSchema
        user = cls(**dict(obj))

        # Add the user instance to the session
        db.add(user)

        try:
            # Attempt to commit changes to the database
            await db.commit()
        except:
            # If an error occurs during commit, rollback the changes
            await db.rollback()
            # Raise an HTTPException to indicate a bad request
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")

        # Return the user instance
        return user

    @classmethod
    async def get_by_id(cls, id: int):
        # Execute a SELECT query to retrieve a user by their ID
        user = await db.execute(select(cls).where(cls.id == id))
        # Return the user as a scalar result (or Raise an HTTPException if not found)
        user = user.scalar_one_or_none()
        if user is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

        return user

    @classmethod
    async def update(cls, obj: dict):
        # Execute an UPDATE query to update a user by their ID
        await db.execute(update(cls).where(cls.id == obj['id']).values(obj))
        # Commit the changes to the database
        try:
            await db.commit()
        except:
            await db.rollback()
            # Raise an HTTPException to indicate server error
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")

        return obj

    @classmethod
    async def delete(cls, id: int):
        # Execute a DELETE query to delete a user by their ID
        await db.execute(delete(cls).where(cls.id == id))
        # Commit the changes to the database
        try:
            await db.commit()
        except:
            await db.rollback()
            # Raise an HTTPException to indicate server error
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")

        return True
    
    @classmethod
    async def get_by_email_or_username(cls, param: str):
        # Execute a SELECT query to retrieve a user by their email or username
        user = await db.execute(select(cls).where(or_(cls.email == param, cls.username == param)))
        # Return the user as a scalar result (or Raise an HTTPException if not found)
        user = user.scalar_one_or_none()
        if user is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

        return user
    
    @classmethod
    async def get_by_token(cls, token: str):
        # Execute a SELECT query to retrieve a user by their token
        user = await db.execute(select(cls).where(cls.token == token))
        # Return the user as a scalar result (or Raise an HTTPException if not found)
        user = user.scalar_one_or_none()
        if user is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")

        return user
    
    @staticmethod
    async def commit():
        try:
            await db.commit()
        except:
            await db.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")