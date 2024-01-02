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
        # return self.reviews.Customer
        pass
    
    @classmethod
    def fanciest(cls):
        best_restaurant=  session.query(cls).order_by(desc(cls.price)).first()
        return best_restaurant
        
    def all_reviews(self):    
        # all_data=session.query(R)
        pass
         