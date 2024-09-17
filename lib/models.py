from sqlalchemy import ForeignKey,Column, Integer, String, DateTime, func
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, relationship
from sqlalchemy.ext.associationproxy import association_proxy

engine = create_engine('sqlite:///musicdata.db')

Session = sessionmaker(bind=engine)
session = Session()

class Base(DeclarativeBase):
    pass


class Concert(Base):
    __tablename__ = 'concerts'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    date = Column(String())
    band_id = Column(Integer(), ForeignKey('bands.id'))
    venue_id = Column(Integer(), ForeignKey('venues.id'))

    band = relationship('Band', back_populates='concerts')
    venue = relationship('Venue', back_populates='concerts')
    
    # method that returns true if the concert is in the band's hometown and false if not
    def hometown_show(self):
        return self.band.hometown == self.venue.city
    
    # method that returns a string with the band's intro for the band
    def introduction(self):
        return f"Hello {self.venue.city}!!! We are {self.band.name} and we're from {self.band.hometown}"
           
    def __repr__(self):
        return f'{self.id} {self.name}'

class Band(Base):
    __tablename__ = 'bands'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    hometown = Column(String())

    concerts = relationship('Concert', back_populates='band')
    venues = association_proxy('concerts', 'venue')

    # method that takes a venue instance and date to create a new concert for the band
    def play_in_venue(self, venue, date):
        if isinstance (venue, Venue) and isinstance(date,str):
            concert = Concert(band=self, venue=venue, date=date)
            return concert
        else: 
            raise TypeError('V')

    # method that returns an array or strings
    def all_introductions(self):
        return [concert.introduction() for concert in self.concerts]
    
    # class method to return the Band instance for the band that has played the most concerts
    @classmethod
    def most_performance(cls):
        performed_count = session.query(cls, func.count(Concert.id)).join(Concert).group_by(cls.id).all()
        performing_band = max(performed_count, key=lambda x:x[1])[0]
        return performing_band

    def __repr__(self):
        return f'id = {self.id}, Band = {self.name}, hometown = {self.hometown} '

class Venue(Base):
    __tablename__ = 'venues'

    id = Column(Integer(), primary_key=True)
    title = Column(String())
    city = Column(String())


    concerts = relationship('Concert', back_populates='venue')
    bands = association_proxy('concerts', 'band')

    # method that finds and returns the first concert on that date at that venue
    def concert_on(self, date):
        return session.query(Concert).filter_by(Concert.venue_id == self.id, Concert.date == date).first()

    
    def most_frequent_band(self):
        frequent_count = session.query(self, func.count(Band.id)).join(Band).group_by(self.id).all()
        frequent_band = max(frequent_count, key=lambda x:x[1])[0]
        return frequent_band

    def __repr__(self):
        return f'id = {self.id}, venue = {self.title}, city = {self.city}'