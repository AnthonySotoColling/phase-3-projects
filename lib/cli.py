from helpers import *


def main_menu():
    choice = 0
    while choice !=3:
        print("Welcome to Tonys epic video game store. We have the best deals and latest games!")
        print("1. Look at all of our games!")
        print("2. Know what you want? order a game!")
        print("3. quit.")
        choice = input()

        if choice == "1":
            all_games()
        elif choice == "2":
            select_and_add_game_to_order()
        elif choice == "3":
            break
        else:
            print("invalid choice")

        
def all_games():
    games = get_all_games()
    for game in games:
        print(f"{game.id} | {game.title} | in stock: {game.stock} | rating: {game.rating} | price: {game.price}")
    print("1.see something you like? order a game.")
    print("2.return to main menu.")
    choice = input()
    if choice == "1":
        select_and_add_game_to_order()
    else:
        main_menu()

def select_and_add_game_to_order(order = None):
    if order is None:
        order = Order(total=0)

    print("Select a game to add to the order:")
    games = get_all_games()
    for game in games:
        print(f"{game.id} | {game.title} | price: {game.price}")
    print("0. Continue to checkout")

    game_id = int(input("Enter the ID of the game: "))
    
    if game_id == 0 and order.total > 0:
        cart(order)
    elif game_id != 0:
        game = session.query(Game).filter_by(id=game_id).first()
        
        if game:
            order.total += game.price
            session.add(order)
            session.commit()
            add_game_to_order(order, game)
            print(f"{game.title} added to the order.")
        else:
            print("Invalid game ID. Please select a valid game.")
        
        select_and_add_game_to_order(order)
    else:
        print("No games in cart.")
        select_and_add_game_to_order(order)

def cart(order):
    print("Games in your cart:")
    for game in order.games:
        print(f"{game.id} | {game.title} | price: {game.price}")
    print(f"Total: {order.total}")
    print("1. Delete a game from cart")
    print("0. Continue to checkout")
    
    choice = input("Enter your choice: ")
    if choice == "1":
        delete_game(order)
    elif choice == "0":
        delivery()
    else:
        print("Invalid choice.")
        cart(order)

def delete_game(order):
    game_id_to_order_item_id ={}
    print("Select a game to remove from your order:")
    games = items_in_cart(order)
    for order_item in games:
        game = order_item.game 
        game_id_to_order_item_id[game.id] = order_item.id
        print(f"{game.id} | {game.title} | price: {game.price}")
    game_id = int(input("Enter the ID of the game to delete: "))
    print(game_id)
    if game_id in game_id_to_order_item_id.keys():
        
        deleted_game = delete_game_from_order(game_id_to_order_item_id[game_id], order)
        if deleted_game:
            print(f"{deleted_game.title} removed from the order.")
    else:
        print("Invalid game ID. Please select a valid game.")
        
    cart(order)



def delivery():
    print("games are curretly being handled with care please be patient while we fill this order.")




 


            









if __name__ == "__main__":
   while True:
        main_menu()
        choice = input()
        if choice == "1":
            all_games()
        elif choice == "2":
            select_and_add_game_to_order()
        
       