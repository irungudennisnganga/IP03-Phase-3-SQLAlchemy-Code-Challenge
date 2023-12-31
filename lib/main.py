from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import restaurant,review , customer 


engine = create_engine("sqlite:///database.db")  
Session = sessionmaker(bind=engine)
session = Session()

# print("Customers Examples")

# rest=session.query(customer.Customer).limit(5).all()
# print(rest)

# customer_1=session.query(customer.Customer).first().restaurant
# review_1=session.query(customer.Customer).first().reviewss
# full_names=customer.Customer.full_name

# print(customer_1)
# print(review_1)
# print(full_names)


# print("Restaurants Example")

# restaurant_1=session.query(restaurant.Restaurant).first().reviewss
# restaurant_customer=session.query(restaurant.Restaurant).first().customer

# print(restaurant_1)
# print(restaurant_customer)

# print("Review Examples")

# review_customer =session.query(review.Review).first().customers
# review_restaurant =session.query(review.Review).first().restaurants


# print(review_customer)
# print(review_restaurant)


session.close()
