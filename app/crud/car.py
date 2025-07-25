from sqlalchemy.orm import Session
from app.models.car import Car  # ✅ Import directo del modelo
from app.schemas.car import CarCreate


def create_car(db: Session, car: CarCreate):
    db_car = Car(**car.dict())
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car


def get_cars(db: Session):
    return db.query(Car).all()  # ✅ Ya no uses models.Car


def delete_car_by_plate(db: Session, plate: str):
    car = db.query(Car).filter(Car.plate == plate).first()
    if car:
        db.delete(car)
        db.commit()
    return car
