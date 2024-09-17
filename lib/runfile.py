from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Concert, Band, Venue



engine = create_engine('sqlite:///musicdata.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

first_band = Band(name='Bukina', hometown='Kikuyu')
first_venue = Venue(title='Kenya Cinema', city='Kikuyu')
first_concert = Concert(name='Sifa', date="7,9,28", band=first_band, venue=first_venue)


print(first_concert.introduction())
print(first_concert.hometown_show())
print(first_band.all_introductions())

bands = session.query(Band).all()
venues = session.query(Venue).all()
print(bands)
print(venues)



