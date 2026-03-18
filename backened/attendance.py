from employee import employee

attendance = {
    1: {"01-01-2026": "Present", "02-01-2026": "Present", "03-01-2026": "Present"},
    2: {"01-01-2026": "Present", "02-01-2026": "Present", "03-01-2026": "Present"},
    3: {"01-01-2026": "Present", "02-01-2026": "Absent", "03-01-2026": "Present"}
}

work_hours = {
    1: {"01-01-2026": 8, "02-01-2026": 8, "03-01-2026": 8},
    2: {"01-01-2026": 8, "02-01-2026": 8, "03-01-2026": 8},
    3: {"01-01-2026": 8, "02-01-2026": 0, "03-01-2026": 8}
}

# Mark attendance
def mark_attendance(emp_id, date, status):
    if not any(emp["id"] == emp_id for emp in employee):
        return {"error": "Employee not found"}

    if emp_id not in attendance:
        attendance[emp_id] = {}

    if date in attendance[emp_id]:
        return {"error": "Attendance already marked"}

    attendance[emp_id][date] = status
    return {"success": "Attendance marked"}

# Record work hours
def record_work_hours(emp_id, date, hours):
    if not any(emp["id"] == emp_id for emp in employee):
        return {"error": "Employee not found"}

    if hours <= 0:
        return {"error": "Invalid working hours"}

    if emp_id not in work_hours:
        work_hours[emp_id] = {}

    if date in work_hours[emp_id]:
        return {"error": "Work hours already recorded for this date"}

    work_hours[emp_id][date] = hours
    return {"success": "Work hours recorded"}

# Monthly attendance
def monthly_attendance(emp_id, month):
    if emp_id not in attendance:
        return {"error": "No attendance found"}

    report = {date: status for date, status in attendance[emp_id].items() if month in date}
    return report if report else {"error": "No records for this month"}                                                 
   