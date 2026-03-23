👨‍💼 Employee Attendance & Salary Management System


🚀 Overview

This is a Employee Attendance Management System built using Streamlit (frontend) and FastAPI (backend). The application allows managing employees, tracking attendance, recording work hours, and calculating salaries with bonus


🌐 Features

➕ Add new employees
📋 View all employees
🔍 Search employee by ID or Name
✏️ Update employee salary
❌ Delete employee
📅 Mark daily attendance
⏱ Record working hours
📊 Monthly attendance report

💰 Calculate salary with:
Bonus (based on attendance)
Deduction (for low attendance)


🛠 Tech Stack

Python
Streamlit (Frontend UI)
Data Structures (List, Dictionary)
FastApi (Backned API)


▶️ How to Run
🔹 1. Clone Repository
git clone 
cd employee-attendance

🔹 2. Install Dependencies
pip install -r requirements.txt

🔹 3. Run Backend (FastAPI)
uvicorn backend.main:app --reload

🔹 4. Run Frontend (Streamlit)
streamlit run frontend/main.py

🔗 API Endpoints (FastAPI)
Method	Endpoint	Description

GET	/employees	Get all employees
POST	/add-employee	Add employee
GET	/search-by-id	Search by ID
GET	/search-by-name	Search by name
PUT	/update-salary	Update salary
DELETE	/delete-employee	Delete employee
POST	/mark-attendance	Mark attendance
POST	/work-hours	Record work hours
GET	/monthly-attendance	Monthly report
GET	/salary	Calculate salary


💼 Resume Highlights

Built a Employee Management System using Streamlit and FastAPI
Designed APIs for employee, attendance, and salary management
Implemented attendance tracking and salary calculation logic with bonus/deduction
Structured project with separate frontend and backend architecture
Developed interactive UI for real-time data management


👨‍💻 Author

MAHERA SHAIKH - https://github.com/05maherashaikh

