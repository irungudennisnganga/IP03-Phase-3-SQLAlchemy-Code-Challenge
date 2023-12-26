from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.base import Base
from models.restaurant import Restaurant
from models.customer import Customer
from models.review import Review

# Create Faker instance to generate random data for our databse
fake = Faker()

# Connect to the database
engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()
session.query(Customer).delete()
session.query(Review).delete()
session.query(Restaurant).delete()

# Generate restaurants
restaurants = [
    Restaurant(
        name=fake.company(),
        price=random.randint(1, 4) 
    )
    for _ in range(10)
]

session.add_all(restaurants)

# Generate customers
customers = [
    Customer(
        first_name=fake.first_name(),
        last_name=fake.last_name()
    )
    for _ in range(20)
]

session.add_all(customers)

# Generate reviews
for _ in range(50):
    review = Review(
        star_rating=random.randint(1, 5), 
        restaurant=random.choice(restaurants),
        customer=random.choice(customers),
    )
    session.add(review)


session.commit()


session.close()
