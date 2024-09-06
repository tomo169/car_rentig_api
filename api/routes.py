from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.auth import get_current_user, oauth2_scheme
from models import User
from dependencies import get_db
from crud import (create_car, get_car, get_cars, update_car, delete_car,
                      create_customer, get_customer, get_customers, update_customer, delete_customer,
                      create_rental, get_rental, get_rentals, delete_rental)

router = APIRouter()

# Routes for Car
@router.post("/cars/")
def create_new_car(make: str, model: str, year: int, license_plate: str, db: Session = Depends(get_db),token: str = Depends(oauth2_scheme)):
    return create_car(db, make, model, year, license_plate)

@router.get("/cars/{car_id}")
def read_car(car_id: int, db: Session = Depends(get_db),token: str = Depends(oauth2_scheme)):
    car = get_car(db, car_id)
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")
    return car

@router.get("/cars/")
def read_cars(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return get_cars(db, skip=skip, limit=limit)

@router.put("/cars/{car_id}")
def update_car_data(car_id: int, update_data: dict, db: Session = Depends(get_db),token: str = Depends(oauth2_scheme)):
    return update_car(db, car_id, update_data)

@router.delete("/cars/{car_id}")
def delete_car_data(car_id: int, db: Session = Depends(get_db),token: str = Depends(oauth2_scheme)):
    return delete_car(db, car_id)

# Routes for Customer
@router.post("/customers/")
def create_new_customer(name: str, email: str, phone_number: str = None, db: Session = Depends(get_db),token: str = Depends(oauth2_scheme)):
    return create_customer(db, name, email, phone_number)

@router.get("/customers/{customer_id}")
def read_customer(customer_id: int, db: Session = Depends(get_db),token: str = Depends(oauth2_scheme)):
    customer = get_customer(db, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@router.get("/customers/")
def read_customers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db),token: str = Depends(oauth2_scheme)):
    return get_customers(db, skip=skip, limit=limit)

@router.put("/customers/{customer_id}")
def update_customer_data(customer_id: int, update_data: dict, db: Session = Depends(get_db),token: str = Depends(oauth2_scheme)):
    return update_customer(db, customer_id, update_data)

@router.delete("/customers/{customer_id}")
def delete_customer_data(customer_id: int, db: Session = Depends(get_db),token: str = Depends(oauth2_scheme)):
    return delete_customer(db, customer_id)

# Routes for Rental
@router.post("/rentals/")
def create_new_rental(customer_id: int, car_id: int, start_time, end_time, db: Session = Depends(get_db),token: str = Depends(oauth2_scheme)):
    return create_rental(db, customer_id, car_id, start_time, end_time)

@router.get("/rentals/{rental_id}")
def read_rental(rental_id: int, db: Session = Depends(get_db),token: str = Depends(oauth2_scheme)):
    rental = get_rental(db, rental_id)
    if not rental:
        raise HTTPException(status_code=404, detail="Rental not found")
    return rental

@router.get("/rentals/")
def read_rentals(skip: int = 0, limit: int = 10, db: Session = Depends(get_db),token: str = Depends(oauth2_scheme)):
    return get_rentals(db, skip=skip, limit=limit)

@router.delete("/rentals/{rental_id}")
def delete_rental_data(rental_id: int, db: Session = Depends(get_db),token: str = Depends(oauth2_scheme)):
    return delete_rental(db, rental_id)
