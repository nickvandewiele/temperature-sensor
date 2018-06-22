import datetime

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, DateTime, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

url_rpi = 'mysql://rpi:raspberry@192.168.0.194/testdb'
engine = create_engine(url_rpi, echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)

class Temperature(Base):
    __tablename__ = 'temperatures'
    id = Column(Integer, primary_key=True)
    dt = Column(DateTime)
    value = Column(Float)
    
    def __repr__(self):
       return "<Temperature(date='%s', value='%s')>" % (
                            self.dt, self.value)

def write(value):

    session = Session()

    t1 = Temperature(dt = datetime.datetime.now(), value = value)
    session.add(t1)
    session.commit()

    print('Successfully written Temperature: {} to DB!'.format(value))