# -*- encoding: utf-8 -*-
"""
Utils functions to make manipulation with the postgresql database
"""
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# These env variables are the same ones used for the DB container
user = os.environ.get('POSTGRES_USER')
pwd = os.environ.get('POSTGRES_PASSWORD')
db = os.environ.get('POSTGRES_DB')
# docker-compose creates a hostname alias with the service name
host = 'postgres'
port = '5432'
engine = create_engine(f'postgresql://{user}:{pwd}@{host}:{port}/{db}')

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.
    from app.models.country import Country, CountrySchema

    Base.metadata.create_all(bind=engine)
