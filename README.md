# 🅿️ Parking Manager App

A simple executable Parking Management System built with **FastAPI**, **SQLite** (via SQLAlchemy), and **Tkinter**. Designed for small use cases where vehicles are registered by license plate, owner's name, and estimated hours of stay, with automatic cost calculation.

---

## 🚀 Features

- Register new vehicles with license plate, owner, hours, and price/hour
- View a live table of all parked vehicles
- Calculate total cost automatically
- Remove vehicles by license plate
- Desktop GUI built with Tkinter
- Backend powered by FastAPI and SQLite

---

## 📦 Stack

- **Backend**: FastAPI + SQLAlchemy + SQLite
- **Frontend**: Tkinter (Python GUI)

---

Author
Built by Tomas Vales as part of a practical portfolio for backend development.

<img width="994" height="447" alt="image" src="https://github.com/user-attachments/assets/2f57e118-ea51-4c0f-9d2c-254bea7dcc84" />


## ▶️ How to Run

1. Start the backend API:

```bash
uvicorn app.main:app --reload
python app/tk_parking.py

