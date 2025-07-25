from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud
from app.database import SessionLocal, engine, Base
from app.models import car as car_model
from app.schemas.car import Car, CarCreate


Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/cars", tags=["cars"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=Car)
def create_car(car: CarCreate, db: Session = Depends(get_db)):
    return crud.create_car(db, car)


@router.get("/", response_model=list[Car])
def list_cars(db: Session = Depends(get_db)):
    return crud.get_cars(db)


@router.delete("/{plate}", response_model=Car)
def delete_car(plate: str, db: Session = Depends(get_db)):
    car = crud.delete_car_by_plate(db, plate)
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")
    return car
