from pydantic import BaseModel
from datetime import datetime


class CarBase(BaseModel):
    plate: str
    owner: str
    hours: int
    price_per_hour: float


class CarCreate(CarBase):
    pass


class Car(CarBase):
    id: int
    timestamp_in: datetime

    class Config:
        orm_mode = True
