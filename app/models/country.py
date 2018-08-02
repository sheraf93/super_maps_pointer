# -*- encoding: utf-8 -*-

from marshmallow import Schema, fields
from sqlalchemy import Column, String, Integer
from sqlalchemy_utils import Timestamp

from app.database import Base

class Country(Base, Timestamp):
    __tablename__ = 'countries'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    capital = Column(String)

    def __init__(self, name=None, capital=None):
        self.name = name
        self.capital = capital


class CountrySchema(Schema):
    id = fields.Number()
    name = fields.Str()
    capital = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()