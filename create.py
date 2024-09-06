from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


db_user = 'root'  
db_password = 'Asdf123' 
db_host = 'localhost'  
db_port = '3308'  
db_name = 'up_ispit'  

db_url = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
engine = create_engine(db_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    email = Column(String(50), unique=True)
    phone_number = Column(String(50), nullable=True)
    
    # Relationship with Rental
    rentals = relationship("Rental", back_populates="customer")

class Car(Base):
    __tablename__ = 'cars'
    
    id = Column(Integer, primary_key=True, index=True)
    make = Column(String(50), index=True)
    model = Column(String(50), index=True)
    year = Column(Integer)
    license_plate = Column(String(50), unique=True)
    is_available = Column(Boolean, default=True)
    
    # Relationship with Rental
    rentals = relationship("Rental", back_populates="car")

class Rental(Base):
    __tablename__ = 'rentals'
    
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    car_id = Column(Integer, ForeignKey('cars.id'))
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    
    # Relationships
    customer = relationship("Customer", back_populates="rentals")
    car = relationship("Car", back_populates="rentals")

def create_tables():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_tables()