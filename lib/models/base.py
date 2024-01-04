#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# from . import restaurant,review , customer

engine = create_engine('sqlite:///database.db')
Session = sessionmaker(bind=engine)
session = Session()

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)
