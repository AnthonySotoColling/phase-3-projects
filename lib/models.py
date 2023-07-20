from sqlalchemy import (PrimaryKeyConstraint, Column, String, Integer)
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()

class games(base):
    __tablename__ = "games"
    __table_args__ = (PrimaryKeyConstraint("id"),)

    id = Column(Integer())
    title = Column(String())
    stock = Column(Integer())
    rating = Column(Integer())
    price = Column(Integer())

    def __repr__(self):
        return f"ID: {self.id}, " \
        + f"Title: {self.title} " \
        + f"Stock: {self.stock} " \
        + f"Rating: {self.rating} " \
        + f"Price: {self.price} "