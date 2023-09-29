from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# Define the database connection string (replace with your own connection details)
db_url = "postgresql://username:password@localhost/mydatabase"

# Create an SQLAlchemy engine
engine = create_engine(db_url)

# Define the declarative base
Base = declarative_base()

# Define the 'orders' table
class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    order_number = Column(Integer)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    customer = relationship("Customer", back_populates="orders")

# Define the 'customers' table
class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    orders = relationship("Order", back_populates="customer")

# Create tables in the database
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

try:
    # Perform an INNER JOIN between 'orders' and 'customers' tables
    result = session.query(Order, Customer).join(Customer, Order.customer_id == Customer.id).all()

    # Process the query result
    for order, customer in result:
        print(f"Order Number: {order.order_number}, Customer Name: {customer.name}")

except Exception as e:
    # Handle exceptions
    print(f"An error occurred: {e}")

finally:
    # Close the session
    session.close()
