from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
import bcrypt
from database import Base

# Define the User model
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"


def hash_password(password: str) -> bytes:
    """Hashes a plain-text password."""
    password_bytes = password.encode('utf-8')
    hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return hashed

def check_password(plain_password: str, hashed_password: bytes) -> bool:
    """Checks if a plain-text password matches a hashed password."""
    plain_password_bytes = plain_password.encode('utf-8')
    return bcrypt.checkpw(plain_password_bytes, hashed_password)

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