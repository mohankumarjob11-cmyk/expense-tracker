import pandas as pd
from app.database import expense_collection

def generate_excel_report():
    data = list(expense_collection.find({}, {"_id": 0}))
    df = pd.DataFrame(data)

    file_path = "expenses_report.xlsx"
    df.to_excel(file_path, index=False)

    return file_path
