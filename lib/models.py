#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey, Table, MetaData  

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///database.db')

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)




class Restaurant(Base):
    __tablename__ = 'restaurants'
    
    id=Column(Integer, primary_key=True)
    name=Column(String)
    price=Column(Integer)
    
    reviews = relationship("Review", back_populates="restaurant")
    
    
    def __repr__(self):
        return f"Restaurant {self.id}: " \
            + f"{self.name}, " \
            + f"Price {self.price}"
    
    
class Customer(Base):
    __tablename__ = 'customers'
    
    id=Column(Integer, primary_key=True)
    first_name=Column(String)
    last_name=Column(String)


    
    reviews = relationship("Review", back_populates="customer")
    
    def __repr__(self):
        return f"Customer {self.id}: " \
            + f"First name {self.first_name}, " \
            + f"Last name {self.last_name}, " \
        
    
class Review(Base):
    __tablename__ = 'reviews'
    
    id=Column(Integer, primary_key=True)
    star_rating=Column(Integer)
    
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"))
    restaurant = relationship("Restaurant", back_populates="reviews")

    customer_id = Column(Integer, ForeignKey("customers.id"))
    customer = relationship("Customer", back_populates="reviews")

    
    
    def __repr__(self):
        return f"Review {self.id}: " \
            + f"Restaurant Id{self.restaurant_id}, " \
            + f"Customer Id {self.customer_id}" \
            + f"Star Rating {self. star_rating}"   
        
         

        