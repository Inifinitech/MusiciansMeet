from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

class Concert():
    __tablename__ = 'concerts'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    

    def band(self):
        pass

    def venue(self):
        pass
