# -*- encoding: utf-8 -*-

from sqlalchemy import Column, String
from sqlalchemy_utils import Timestamp

class Country(Base, Timestamp):
    __tablename__ = 'countries'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    capital = Column(String)