#!/usr/bin/env python3
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base,session
from .review import Review
import random



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

    #  should return a collection of all the reviews that the `Customer` has left
    def reviewss(self):
        return self.reviews
    
    def restaurant(self):
        all_restaurant = []
        for one_restaurant in self.reviews:
            all_restaurant.append(
               one_restaurant.restaurant.name
            )
        return all_restaurant
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
       
    def favourite_restaurant(self):
        highest_rating = max(rate.star_rating for rate in self.reviews)
        fav_restaurant = [ fav.restaurant for fav in self.reviews if fav.star_rating == highest_rating ]
        return random.choice(fav_restaurant) if fav_restaurant else None  
   
    def add_review(self,restaurant,rating):
        new_review = Review(
            # Remeber to correct here on customer_id's so that it caan automatically grab the customer's id
            customer_id=12,
            restaurant_id=restaurant,
            star_rating=rating
        )
        session.add(new_review)
        session.commit()
        return new_review
    
    #takes a `restaurant` (an instance of the `Restaurant` class) and

    # removes **all** their reviews for this restaurant

    # you will have to delete rows from the `reviews` table to get this to work!
    
    def delete_reviews(self,restaurant):
        review_to_delete=[ review for review in self.reviews if review.restaurant_id == restaurant ]
        
        for review in review_to_delete :
            session.delete(review)
        session.commit()   
        # delete_review = session.query(Review).filter_by((Review.restaurant_id) ).all()
        # print(delete_review)