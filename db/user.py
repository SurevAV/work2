from sqlalchemy import Column, BigInteger, Integer, Boolean, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
from db.base import Base
from datetime import datetime

class User(Base):
    __tablename__ = 'user'
    id = Column(BigInteger, primary_key=True,autoincrement=True)
    name = Column(String, nullable=True)
    lesson = Column(BigInteger,nullable=True)
    idTelegram = Column(String,nullable=True)
    lastDate = Column(DateTime,nullable=True)
    idChat = Column(String, nullable=True)
    paid = Column(BigInteger,nullable=True)
