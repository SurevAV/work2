from sqlalchemy import Column, BigInteger, String, DateTime
from db.base import Base

class Login(Base):
    __tablename__ = 'login'
    id = Column(BigInteger, primary_key=True,autoincrement=True)
    token = Column(String, nullable=True)
    toDate = Column(DateTime, nullable=True)

