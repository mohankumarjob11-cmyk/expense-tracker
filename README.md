📊 Expense Tracker API

A backend Expense Tracker application built using FastAPI and MongoDB, which allows users to manage daily expenses, generate category-wise summaries, and download reports.

🚀 Features

✅ Create, Read, Update, Delete (CRUD) expenses

📅 Track expenses with date, category, amount, payment mode, etc.

📊 Category-wise expense summary using MongoDB aggregation

📁 Export expenses as an Excel report

⚡ FastAPI with automatic Swagger UI

☁️ MongoDB Atlas cloud database

🛠 Tech Stack

Backend Framework: FastAPI

Database: MongoDB (Atlas)

ODM/Driver: PyMongo

Language: Python 3.10+

Reporting: Pandas + Excel

Server: Uvicorn

📂 Project Structure
expense-tracker/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── schemas.py
│   ├── crud.py
│   ├── routes/
│   │   └── expenses.py
│   └── reports/
│       └── excel_report.py
│
├── requirements.txt
├── README.md
└── venv/

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/expense-tracker.git
cd expense-tracker

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure MongoDB

Update database.py with your MongoDB Atlas connection string:

MONGO_URI = mongodb+srv://mohankumart_db_user:lkWXZizGNuFNFd9s@cluster0.ongqzhp.mongodb.net/?appName=Cluster0


5️⃣ Run the Application
uvicorn app.main:app --reload

🌐 API Documentation

Once the server is running, open:

Swagger UI:
👉 http://127.0.0.1:8000/docs

🔗 API Endpoints
➕ Create Expense

POST /expenses

📄 Get All Expenses

GET /expenses

🔍 Get Expense by ID

GET /expenses/{expense_id}

✏️ Update Expense

PUT /expenses/{expense_id}

❌ Delete Expense

DELETE /expenses/{expense_id}

📊 Category Summary

GET /expenses/summary/category

📥 Download Excel Report

GET /expenses/report/excel

🧪 Sample Request (POST)
{
  "expense_date": "2026-01-08",
  "category": "Food",
  "amount": 250.75,
  "description": "Lunch",
  "payment_mode": "UPI",
  "merchant_name": "Cafe XYZ",
  "location": "Chennai",
  "notes": "Office lunch",
  "created_by": "Mohankumar"
}

📈 Sample Category Summary Response
[
  {
    "category": "Food",
    "total_amount": 1250.75
  },
  {
    "category": "Transport",
    "total_amount": 600
  }
]

📌 Future Enhancements

🔐 Authentication & User accounts

📅 Monthly/Yearly reports

📄 PDF report generation

📱 Frontend using React



⭐ Conclusion

This project demonstrates:

RESTful API design

MongoDB aggregation pipelines

Report generation

Clean backend architecture
