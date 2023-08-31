from sqlalchemy import create_engine
from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship, backref, declarative_base
# from sqlalchemy.ext.declarative import
from sqlalchemy.orm import sessionmaker

# from models import Game, Review
engine = create_engine('sqlite:///one_to_many.db')

Base = declarative_base()

class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer(), primary_key=True)
    title = Column(String())
    genre = Column(String())
    platform = Column(String())
    price = Column(Integer())

    reviews = relationship('Review', backref=backref('game'), cascade='all, delete-orphan')

    def __repr__(self):
        return f'Game(id={self.id}, ' + \
            f'title={self.title}, ' + \
            f'platform={self.platform})'

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer(), primary_key=True)
    score = Column(Integer())
    comment = Column(String())

    game_id = Column(Integer(), ForeignKey('games.id'))

    def __repr__(self):
        return f'Review(id={self.id}, ' + \
            f'score={self.score}, ' + \
            f'game_id={self.game_id})'



if __name__ == '__main__':
    engine = create_engine('sqlite:///one_to_many.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    review = session.query(Review).first()
    print(review)

    reviews = session.query(Review).filter_by(game_id = 2).all()
    print(reviews)

    game = session.query(Game).filter(Game.id==3).first()
    session.delete(game)
    print(game.reviews)
