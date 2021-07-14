from sqlalchemy import Column, Integer, String, Boolean,Date, ForeignKey

from app.database.base_class import Base


class Item(Base):
    id = Column(Integer,primary_key = True, index=True, autoincrement=True)
    name = Column(String, primary_key=True)
    price = Column(Integer)