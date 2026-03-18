# frontend/main.py

import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("Employee Management System (Frontend)")

menu = st.sidebar.selectbox(
    "Menu",
    ["Add Employee","View Employees","Search Employee","Update Salary","Delete Employee",
     "Mark Attendance","Record Work Hours","Monthly Attendance","Calculate Salary"]
)

# -------- ADD EMPLOYEE --------
if menu == "Add Employee":
    st.subheader("Add Employee")

    emp_id = st.number_input("Employee ID")
    name = st.text_input("Name")
    position = st.text_input("Position")
    department = st.text_input("Department")
    salary = st.number_input("Salary")

    if st.button("Add"):
        res = requests.post(
            f"{API_URL}/add-employee",
            params={
                "emp_id": emp_id,
                "name": name,
                "position": position,
                "department": department,
                "salary": salary
            }
        )
        st.success(res.json()["message"])

# -------- VIEW EMPLOYEES --------
elif menu == "View Employees":
    res = requests.get(f"{API_URL}/employees")
    st.dataframe(res.json())

# -------- SEARCH --------
elif menu == "Search Employee":
    option = st.selectbox("Search by", ["ID", "Name"])

    if option == "ID":
        emp_id = st.number_input("Employee ID")
        if st.button("Search"):
            res = requests.get(f"{API_URL}/search-by-id", params={"emp_id": emp_id})
            st.write(res.json())
    else:
        name = st.text_input("Name")
        if st.button("Search"):
            res = requests.get(f"{API_URL}/search-by-name", params={"name": name})
            st.write(res.json())

# -------- UPDATE SALARY --------
elif menu == "Update Salary":
    emp_id = st.number_input("Employee ID")
    new_salary = st.number_input("New Salary")

    if st.button("Update"):
        res = requests.put(
            f"{API_URL}/update-salary",
            params={"emp_id": emp_id, "new_salary": new_salary}
        )
        st.success(res.json()["message"])

# -------- DELETE --------
elif menu == "Delete Employee":
    emp_id = st.number_input("Employee ID")

    if st.button("Delete"):
        res = requests.delete(
            f"{API_URL}/delete-employee",
            params={"emp_id": emp_id}
        )
        st.warning(res.json()["message"])

# -------- ATTENDANCE --------
elif menu == "Mark Attendance":
    emp_id = st.number_input("Employee ID")
    date = st.text_input("Date (DD-MM-YYYY)")
    status = st.selectbox("Status", ["Present", "Absent"])

    if st.button("Submit"):
        res = requests.post(
            f"{API_URL}/mark-attendance",
            params={"emp_id": emp_id, "date": date, "status": status}
        )
        st.write(res.json())

# -------- WORK HOURS --------
elif menu == "Record Work Hours":
    emp_id = st.number_input("Employee ID")
    date = st.text_input("Date")
    hours = st.number_input("Hours")

    if st.button("Submit"):
        res = requests.post(
            f"{API_URL}/work-hours",
            params={"emp_id": emp_id, "date": date, "hours": hours}
        )
        st.write(res.json())

# -------- MONTHLY REPORT --------
elif menu == "Monthly Attendance":
    emp_id = st.number_input("Employee ID")
    month = st.text_input("Month (MM-YYYY)")

    if st.button("View"):
        res = requests.get(
            f"{API_URL}/monthly-attendance",
            params={"emp_id": emp_id, "month": month}
        )
        st.write(res.json())

# -------- SALARY --------
elif menu == "Calculate Salary":
    emp_id = st.number_input("Employee ID")
    month = st.text_input("Month (MM-YYYY)")

    if st.button("Calculate"):
        res = requests.get(
            f"{API_URL}/salary",
            params={"emp_id": emp_id, "month": month}
        )
        st.write(res.json())