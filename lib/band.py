class Band():
    __tablename__ = 'bands'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    def concerts(self):
        pass

    def venues(self):
        pass