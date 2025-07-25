from fastapi import FastAPI
from app.routes import car

app = FastAPI(title="Parking API",
              description="API for managing parking cars", version="1.0.0")


app.include_router(car.router)
