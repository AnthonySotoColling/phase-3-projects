from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import ( Games)


if __name__ == "__main__":
    engine = create_engine("sqlite:///video_games.db")
    #base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    Kid_Chameleon = Games(title="Kid Chameleon", stock= 16, rating= 5, price= 50)
    x_men_genesis = Games(title="x-men genesis", stock= 5, rating= 4, price= 40)
    The_Terminator = Games(title="The Terminator", stock= 20, rating= 4.5, price= 70)
    Decap_Attack = Games(title="Decap Attack", stock= 16, rating= 4.5, price= 40)
    Truxton = Games(title="Truxton", stock= 3, rating= 4.5, price= 100)
    Castle_of_Illusion_Starring_Mickey_Mouse = Games(title="Castle of Illusion Starring Mickey Mouse", stock= 14, rating= 5, price= 35)

    session.bulk_save_objects([Kid_Chameleon, x_men_genesis, The_Terminator, Decap_Attack, Truxton, Castle_of_Illusion_Starring_Mickey_Mouse])
    session.commit()
    #sam = Customers(account_name = "Sam", password= 12345, address="123 Poway Rd 92129", wallet= 50)
    #liz = Customers(account_name = "Liz", password= 34567, address="552 Mira Mar way 92129", wallet= 500)
    #session.bulk_save_objects([sam,liz])
    #session.commit()