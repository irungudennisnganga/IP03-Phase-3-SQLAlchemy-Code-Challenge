#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import restaurant,review , customer 


engine = create_engine("sqlite:///database.db")  
Session = sessionmaker(bind=engine)
session = Session()

print("Customers Examples")

# rest=session.query(customer.Customer).limit(5).all()
# print(rest)

customer_1=session.query(customer.Customer).first()
review_1=session.query(customer.Customer).first()
full_names=session.query(customer.Customer).first()
favourite_restaurants = session.query(customer.Customer).first()

# add_reviews= customer.Customer.add_review(customer.Customer,5,4)

# del_reviews= session.query(customer.Customer).first().delete_reviews


# print(review_1.reviewss())
# print(customer_1.restaurant())
# print(full_names.full_name())
# print(favourite_restaurants.favourite_restaurant())

# customer.Customer.delete_reviews(del_reviews,2)


print("Restaurants Example")

restaurant_1=session.query(restaurant.Restaurant).first()
restaurant_customer=session.query(restaurant.Restaurant).first()
one=session.query(restaurant.Restaurant).first()
all_restaurant_reviws= session.query(restaurant.Restaurant).first()

# print(restaurant_1.reviewss())
# print(restaurant_customer.customer())
# print( one.fanciest())
# print(all_restaurant_reviws.all_reviews())

print("Review Examples")

review_customer =session.query(review.Review).first()
review_restaurant =session.query(review.Review).first()
reviews = session.query(review.Review).first()  


# print(review_customer.customers())
# print(review_restaurant.restaurants())
# print(reviews.full_review()) 



session.close()
