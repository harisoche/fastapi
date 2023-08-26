from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy import false
from database import Base
from datetime import datetime


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