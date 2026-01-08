from fastapi import FastAPI
from app.routes import expenses

app = FastAPI(title="Expense Tracker API")

app.include_router(expenses.router)

@app.get("/")
def root():
    return {"status": "Expense Tracker Running"}
