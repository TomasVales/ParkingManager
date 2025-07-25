from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from app.database import Base


class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, index=True)
    plate = Column(String, unique=True, index=True)
    owner = Column(String)
    hours = Column(Integer)
    price_per_hour = Column(Float)
    timestamp_in = Column(DateTime, default=datetime.utcnow)
