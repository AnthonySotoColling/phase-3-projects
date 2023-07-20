from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import (base, games)


if __name__ == "__main__":
    engine = create_engine("sqlite:///video_games.db")
    base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    Kid_Chameleon = games(title="Kid Chameleon", stock= 16, rating= 5, price= 50)
    x_men_genesis = games(title="x-men genesis", stock= 5, rating= 4, price= 40)
    The_Terminator = games(title="The Terminator", stock= 20, rating= 4.5, price= 70)
    Decap_Attack = games(title="Decap Attack", stock= 16, rating= 4.5, price= 40)
    Truxton = games(title="Truxton", stock= 3, rating= 4.5, price= 100)
    Castle_of_Illusion_Starring_Mickey_Mouse = games(title="Castle of Illusion Starring Mickey Mouse", stock= 14, rating= 5, price= 35)

    #session.bulk_save_objects([Kid_Chameleon, x_men_genesis, The_Terminator, Decap_Attack, Truxton, Castle_of_Illusion_Starring_Mickey_Mouse])
    #session.commit()