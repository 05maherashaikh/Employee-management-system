from employee import employee
from attendance import attendance, work_hours

def calculate_salary(emp_id, month):
    emp_data = next((emp for emp in employee if emp["id"] == emp_id), None)
    if not emp_data:
        return {"error": "Employee not found"}

    days_present = sum(1 for date, status in attendance.get(emp_id, {}).items() if month in date and status=="Present")
    total_hours = sum(hours for date, hours in work_hours.get(emp_id, {}).items() if month in date)

    base_salary = emp_data["salary"]
    bonus = 2000 if days_present >= 5 else 0
    deduction = 1000 if days_present <= 3 else 0
    net_salary = base_salary + bonus - deduction

    return {
        "Employee Name": emp_data["name"],
        "Position": emp_data["position"],
        "Department": emp_data["department"],
        "Month": month,
        "Days Present": days_present,
        "Total Hours Worked": total_hours,
        "Base Salary": base_salary,
        "Bonus": bonus,
        "Deduction": deduction,
        "Net Salary": net_salary
    }              