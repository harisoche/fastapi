from sqlalchemy import Column, Integer, String, DateTime, SmallInteger, Boolean
from sqlalchemy import false, true
from database import Base
from datetime import datetime


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(60), nullable=False)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    token = Column(String(255), nullable=True)
    role_id = Column(SmallInteger, nullable=False)
    is_active = Column(Boolean, nullable=False, default=true())
    is_verified = Column(Boolean, nullable=True, default=false())
    created_at = Column(DateTime, nullable=False, server_default=datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))
    updated_at = Column(DateTime, nullable=False, server_default=datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))

    def __repr__(self):
        return f"<User(fullName={self.full_name})>"