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
host = 'postgres' # docker-compose creates a hostname alias with the service name
port = '5432' # default postgres port 
engine = create_engine(f'postgresql://{user}:{pwd}@{host}:{port}/{db}')

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import app.models

    Base.metadata.create_all(bind=engine)
