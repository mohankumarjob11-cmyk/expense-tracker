from app.database import expense_collection
from bson import ObjectId
from datetime import datetime   # ✅ REQUIRED

def expense_helper(expense) -> dict:
    return {
        "expense_id": str(expense["_id"]),
        "expense_date": expense["expense_date"].date(),
        "category": expense["category"],
        "amount": expense["amount"],
        "description": expense.get("description"),
        "payment_mode": expense["payment_mode"],
        "merchant_name": expense["merchant_name"],
        "location": expense.get("location"),
        "notes": expense.get("notes"),
        "created_by": expense["created_by"]
    }

def create_expense(expense_data: dict):
    expense_data["expense_date"] = datetime.combine(
        expense_data["expense_date"],
        datetime.min.time()
    )
    result = expense_collection.insert_one(expense_data)
    return str(result.inserted_id)

def get_all_expenses():
    return [expense_helper(exp) for exp in expense_collection.find()]

def get_expense_by_id(expense_id: str):
    expense = expense_collection.find_one({"_id": ObjectId(expense_id)})
    return expense_helper(expense) if expense else None

def delete_expense(expense_id: str):
    expense_collection.delete_one({"_id": ObjectId(expense_id)})
def update_expense(expense_id: str, data: dict):
    data["expense_date"] = datetime.combine(
        data["expense_date"],
        datetime.min.time()
    )

    result = expense_collection.update_one(
        {"_id": ObjectId(expense_id)},
        {"$set": data}
    )

    return result.matched_count
def get_category_summary():
    pipeline = [
        {
            "$group": {
                "_id": "$category",
                "total_amount": {"$sum": "$amount"}
            }
        }
    ]
    return [
        {"category": item["_id"], "total_amount": item["total_amount"]}
        for item in expense_collection.aggregate(pipeline)
    ]
