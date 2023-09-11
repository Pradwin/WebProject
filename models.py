from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
import datetime
from .database import Base


class Ambulence(Base):
    __tablename__ = "Ambulence"

    id = Column(Integer, primary_key=True, index=True)
    number_plate=Column(String)
    capacity=Column(Integer)



class Booking(Base):
    __tablename__ = "Booking"

    id = Column(Integer, primary_key=True, index=True)
    pic_loc = Column(String, index=True)
    drop_loc = Column(String, index=True)
    date = Column(datetime.date, index=True)
    requirments = Column(String, index=True)
    email = Column(String, index=True)
    number_plate=Column(String)


