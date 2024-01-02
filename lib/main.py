from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import restaurant,review , customer 


engine = create_engine("sqlite:///database.db")  
Session = sessionmaker(bind=engine)
session = Session()

print("Customers Examples")

# rest=session.query(customer.Customer).limit(5).all()
# print(rest)

# customer_1=session.query(customer.Customer).get(5)
# review_1=session.query(customer.Customer).get(5)
# full_names=session.query(customer.Customer).get(5)
# favourite_restaurants = customer.Customer.favourite_restaurant

# add_reviews= customer.Customer.add_review(customer.Customer,5,4)

# del_reviews= customer.Customer.delete_reviews(restaurant.Restaurant,3)

# print(customer_1.restaurant())
# print(review_1.reviewss())
# print(full_names.full_name())
# print({one for one in favourite_restaurants.__dict__})


print("Restaurants Example")

# restaurant_1=session.query(restaurant.Restaurant).get(4)
# restaurant_customer=session.query(restaurant.Restaurant).first()
# one=session.query(restaurant.Restaurant).first()
# all_restaurant_reviws= session.query(restaurant.Restaurant).get(4)

# print(restaurant_1.reviewss())
# print(restaurant_customer.customer())
# print( one.fanciest())
# print(all_restaurant_reviws.all_reviews())

print("Review Examples")

# review_customer =session.query(review.Review).get(6)
# review_restaurant =session.query(review.Review).get(5)
# reviews = session.query(review.Review).get(9)  


# print(review_customer.customers())
# print(review_restaurant.restaurants())
# print(reviews.full_review()) 



session.close()
