from database import Base
from sqlalchemy import String, Boolean, Integer, Column, Text


class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    description = Column(Text, nullable=False)
    price = Column(Integer, nullable=False)
    on_offer = Column(Boolean, default=False)
