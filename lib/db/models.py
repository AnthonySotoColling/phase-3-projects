from sqlalchemy import (PrimaryKeyConstraint, Column, String, Integer,ForeignKey)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy


Base = declarative_base()

class Game(Base):
    __tablename__ = "games"
    __table_args__ = (PrimaryKeyConstraint("id"),)

    id = Column(Integer())
    title = Column(String())
    stock = Column(Integer())
    rating = Column(Integer())
    price = Column(Integer())
    order_items = relationship('Order_item', back_populates=('game'))
    orders = association_proxy("order_items", "order")

    def __repr__(self):
        return f"ID: {self.id}, " \
        + f"Title: {self.title} " \
        + f"Stock: {self.stock} " \
        + f"Rating: {self.rating} " \
        + f"Price: {self.price} "
    
#class Customers(Base):
   # __tablename__ = "customers"
   # __table_args__ = (PrimaryKeyConstraint("id"),)

    #id = Column(Integer())
    #account_name = Column(String())
    #password = Column(Integer())
    #address = Column(String())
    #wallet = Column(Integer())

    #def __repr__(self):
        #return f"ID: {self.id}, " \
       # + f"account_name: {self.account_name} " \
       # + f"password: {self.password} " \
        #+ f"address: {self.address} " \
       # + f"wallet: {self.wallet} "
    
class Order(Base):
    __tablename__ = "orders"
    __table_args__ = (PrimaryKeyConstraint("id"),)

    id = Column(Integer())
    total = Column(Integer())
    order_items = relationship('Order_item', back_populates=('order'))
    games = association_proxy("order_items", "game")
    

    def __repr__(self):
        return f"ID: {self.id}, " \
        + f"total: {self.total} " \
        + f"order_items: {self.order_items} "
    
class Order_item(Base):
    __tablename__ = "order_items"
    __table_args__ = (PrimaryKeyConstraint("id"),)

    id = Column(Integer())
    game_id = Column(Integer(),ForeignKey("games.id"))
    order_id = Column(Integer(),ForeignKey("orders.id"))
    order = relationship("Order", back_populates=("order_items"))
    game = relationship("Game", back_populates=("order_items"))
    


    def __repr__(self):
        return f"ID: {self.id}, " \
        + f"game_id: {self.game_id} " \
        + f"order_id: {self.order_id} "
        
    