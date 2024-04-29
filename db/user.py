from sqlalchemy import Column, BigInteger, String, DateTime
from db.base import Base

class User(Base):
    __tablename__ = 'user'
    id = Column(BigInteger, primary_key=True,autoincrement=True)
    name = Column(String, nullable=True)
    lesson = Column(BigInteger,nullable=True)
    idTelegram = Column(String,nullable=True)
    lastDate = Column(DateTime,nullable=True)
    idChat = Column(String, nullable=True)
    paid = Column(BigInteger,nullable=True)
