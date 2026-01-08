from fastapi import APIRouter, HTTPException
from app.schemas import ExpenseCreate
from app.crud import create_expense, get_all_expenses, get_expense_by_id, delete_expense, update_expense
from app.crud import get_category_summary
from fastapi.responses import FileResponse
from app.reports.excel_report import generate_excel_report

router = APIRouter()

@router.post("/expenses")
def add_expense(expense: ExpenseCreate):
    expense_id = create_expense(expense.dict())
    return {"message": "Expense created", "expense_id": expense_id}

@router.get("/expenses")
def list_expenses():
    return get_all_expenses()

@router.get("/expenses/{expense_id}")
def get_expense(expense_id: str):
    expense = get_expense_by_id(expense_id)
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    return expense

@router.delete("/expenses/{expense_id}")
def remove_expense(expense_id: str):
    delete_expense(expense_id)
    return {"message": "Expense deleted"}

@router.put("/expenses/{expense_id}")
def update_expense_api(expense_id: str, expense: ExpenseCreate):
    updated = update_expense(expense_id, expense.dict())
    if updated == 0:
        raise HTTPException(status_code=404, detail="Expense not found")
    return {"message": "Expense updated successfully"}

@router.get("/expenses/summary/category")
def category_summary():
    return get_category_summary()

@router.get("/expenses/report/excel")
def download_excel():
    file_path = generate_excel_report()
    return FileResponse(
        path=file_path,
        filename="expenses_report.xlsx",
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

