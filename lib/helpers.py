from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import (Game,Order_item,Order)

engine = create_engine("sqlite:///db/video_games.db")
Session = sessionmaker(bind=engine)
session = Session()

def get_all_games():
    return session.query(Game).all()


def create_order():
    order = Order(total=0)
    session.add(order)
    session.commit()
    return order
    
def add_game_to_order(order, game):
    order_item = Order_item(order_id=order.id, game_id=game.id)
    session.add(order_item)
    session.commit()

def items_in_cart(order):
    return session.query(Order_item).filter_by(order_id= order.id).join(Game).all()
            
# def delete_game_from_order(order_item_id, order):
#     order_item = session.query(Order_item).filter_by(order_item=order_item.id).all()
#     session.delete(order_item.id)
#     session.commit()
    
def delete_game_from_order(order_item_id, order):
    print(order_item_id)
    order_item = session.query(Order_item).filter_by(id=order_item_id).first()
    print(order_item)

    if order_item:
        game = order_item.game
        order.total -= game.price
        session.delete(order_item)
        session.commit()
        return game  
    else:
        return None  
    

