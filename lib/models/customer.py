from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from .base import Base


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    reviews = relationship("Review", back_populates="customer")

    def __repr__(self):
        return (
            f"Customer {self.id}: "
            + f"First name {self.first_name}, "
            + f"Last name {self.last_name}"
        )
