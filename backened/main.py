# backend/main.py

from fastapi import FastAPI
from employee import add_employee, view_all, search_by_id, search_by_name, update_salary, delete_employee
from attendance import mark_attendance, record_work_hours, monthly_attendance
from salary import calculate_salary

app = FastAPI()

# -------- EMPLOYEE --------

@app.get("/employees")
def get_all_employees():
    return view_all()

@app.post("/add-employee")
def add_emp(emp_id: int, name: str, position: str, department: str, salary: float):
    return {"message": add_employee(emp_id, name, position, department, salary)}

@app.get("/search-by-id")
def search_id(emp_id: int):
    return search_by_id(emp_id)

@app.get("/search-by-name")
def search_name(name: str):
    return search_by_name(name)

@app.put("/update-salary")
def update(emp_id: int, new_salary: float):
    return {"message": update_salary(emp_id, new_salary)}

@app.delete("/delete-employee")
def delete(emp_id: int):
    return {"message": delete_employee(emp_id)}

# -------- ATTENDANCE --------

@app.post("/mark-attendance")
def mark(emp_id: int, date: str, status: str):
    return mark_attendance(emp_id, date, status)

@app.post("/work-hours")
def work(emp_id: int, date: str, hours: float):
    return record_work_hours(emp_id, date, hours)

@app.get("/monthly-attendance")
def monthly(emp_id: int, month: str):
    return monthly_attendance(emp_id, month)

# -------- SALARY --------

@app.get("/salary")
def salary(emp_id: int, month: str):
    return calculate_salary(emp_id, month)