from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .base import Base


class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

    reviews = relationship("Review", back_populates="restaurant")

    def __repr__(self):
        return (
            f"Restaurant {self.id}: "
            + f"{self.name}, "
            + f"Price {self.price}"
        )

    def reviewss(self):
        return self.reviews
    
    def customer(self):
        return self.customers