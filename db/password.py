from sqlalchemy import Column, BigInteger, String
from db.base import Base

class Password(Base):
    __tablename__ = 'password'
    id = Column(BigInteger, primary_key=True,autoincrement=True)
    text = Column(String, nullable=True)
