from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import restaurant,review , customer 


engine = create_engine("sqlite:///database.db")  
Session = sessionmaker(bind=engine)
session = Session()


rest=session.query(customer.Customer).limit(5).all()
print([one for one in rest])

session.close()
