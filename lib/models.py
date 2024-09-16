from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

class Concert():
    # __tablename__ = 'concerts'

    # id = Column(Integer(), primary_key=True)
    # name = Column(String())
    

    def band(self):
        pass

    def venue(self):
        pass

class Band():
    __tablename__ = 'bands'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    hometown = Column(String())

    def concerts(self):
        pass

    def venues(self):
        pass

class Venue():
    __tablename__ = 'venues'

    id = Column(Integer(), primary_key=True)
    title = Column(String())
    city = Column(String())

    def concerts(self):
        pass

    def bands(self):
        pass