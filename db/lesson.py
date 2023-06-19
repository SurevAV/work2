from sqlalchemy import Column, BigInteger, Integer, Boolean, ForeignKey, String
from sqlalchemy.orm import relationship
from db.base import Base


class Lesson(Base):
    __tablename__ = 'lessons'
    id = Column(BigInteger, primary_key=True, autoincrement=False)
    video_link = Column(String, nullable=False)
    thesis = Column(String, nullable=False)

