from sqlalchemy import Column, BigInteger, Integer, Boolean, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
from db.base import Base
from datetime import datetime

class Password(Base):
    __tablename__ = 'password'
    id = Column(BigInteger, primary_key=True,autoincrement=True)
    text = Column(String, nullable=True)
