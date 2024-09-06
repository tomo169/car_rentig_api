from sqlalchemy.orm import Session
from models import *
from schemas import UserCreate

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def create_user(db: Session, user: UserCreate, hashed_password: str):
    hashed_password = hash_password(user.password)
    db_user = User(username=user.username, email=user.email, password=hashed_password.decode('utf-8'))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, username: str, password: str):
    user = get_user_by_username(db, username)
    if user and check_password(password, user.password.encode('utf-8')):
        return user
    return None

# CRUD for Car
def create_car(db: Session, make: str, model: str, year: int, license_plate: str):
    car = Car(make=make, model=model, year=year, license_plate=license_plate)
    db.add(car)
    db.commit()
    db.refresh(car)
    return car

def get_car(db: Session, car_id: int):
    return db.query(Car).filter(Car.id == car_id).first()

def get_cars(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Car).offset(skip).limit(limit).all()

def update_car(db: Session, car_id: int, update_data: dict):
    car = db.query(Car).filter(Car.id == car_id).first()
    if car:
        for key, value in update_data.items():
            setattr(car, key, value)
        db.commit()
        db.refresh(car)
    return car

def delete_car(db: Session, car_id: int):
    car = db.query(Car).filter(Car.id == car_id).first()
    if car:
        db.delete(car)
        db.commit()
    return car

# CRUD for Customer
def create_customer(db: Session, name: str, email: str, phone_number: str = None):
    customer = Customer(name=name, email=email, phone_number=phone_number)
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer

def get_customer(db: Session, customer_id: int):
    return db.query(Customer).filter(Customer.id == customer_id).first()

def get_customers(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Customer).offset(skip).limit(limit).all()

def update_customer(db: Session, customer_id: int, update_data: dict):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if customer:
        for key, value in update_data.items():
            setattr(customer, key, value)
        db.commit()
        db.refresh(customer)
    return customer

def delete_customer(db: Session, customer_id: int):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if customer:
        db.delete(customer)
        db.commit()
    return customer

# CRUD for Rental
def create_rental(db: Session, customer_id: int, car_id: int, start_time, end_time):
    rental = Rental(customer_id=customer_id, car_id=car_id, start_time=start_time, end_time=end_time)
    db.add(rental)
    db.commit()
    db.refresh(rental)
    return rental

def get_rental(db: Session, rental_id: int):
    return db.query(Rental).filter(Rental.id == rental_id).first()

def get_rentals(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Rental).offset(skip).limit(limit).all()

def delete_rental(db: Session, rental_id: int):
    rental = db.query(Rental).filter(Rental.id == rental_id).first()
    if rental:
        db.delete(rental)
        db.commit()
    return rental