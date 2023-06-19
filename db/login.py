from sqlalchemy import Column, BigInteger, Integer, Boolean, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
from db.base import Base
from datetime import datetime

class Login(Base):
    __tablename__ = 'login'
    id = Column(BigInteger, primary_key=True,autoincrement=True)
    token = Column(String, nullable=True)
    toDate = Column(DateTime, nullable=True)

