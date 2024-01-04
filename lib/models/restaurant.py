#!/usr/bin/env python3
from sqlalchemy import Column, Integer, String,desc
from sqlalchemy.orm import relationship
from .base import Base,session


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
        all_customers = [ one_customer.customer.full_name() for one_customer in self.reviews]
        return all_customers
        
    
    @classmethod
    def fanciest(cls):
        best_restaurant=  session.query(cls).order_by(desc(cls.price)).first()
        return best_restaurant
        
    def all_reviews(self):    
        all_made_reviews=[]
        
        for one_review in self.reviews:
            all_made_reviews.append(
                f"Review for {self.name} by {one_review.customer.full_name()}: {one_review.star_rating}"
            )
        return all_made_reviews
         