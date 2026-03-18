employee = [
    {"id": 1, "name": "John Doe", "position": "Software Engineer", "department": "Engineering", "salary": 80000},
    {"id": 2, "name": "Jane Smith", "position": "Product Manager", "department": "Product", "salary": 90000},
    {"id": 3, "name": "Alice Johnson", "position": "Data Scientist", "department": "Data", "salary": 85000},
    {"id": 4, "name": "Bob Brown", "position": "UX Designer", "department": "Design", "salary": 75000},
    {"id": 5, "name": "Charlie Davis", "position": "DevOps Engineer", "department": "Operations", "salary": 82000}
]

# Add a new employee
def add_employee(emp_id, name, position, department, salary):
    for emp in employee:
        if emp['id'] == emp_id:
            return "Employee already exists"
    employee.append({
        'id': emp_id,
        'name': name,
        'position': position,
        'department': department,
        'salary': float(salary)
    })
    return "Employee added successfully"

# View all employees
def view_all():
    return employee

# Search employee by ID
def search_by_id(emp_id):
    for emp in employee:
        if emp['id'] == emp_id:
            return emp
    return {"error": "Employee not found"}

# Search employee by name
def search_by_name(name):
    result = [emp for emp in employee if name.lower() in emp['name'].lower()]
    return result if result else {"error": "Employee not found"}

# Update salary
def update_salary(emp_id, new_salary):
    for emp in employee:
        if emp['id'] == emp_id:
            emp['salary'] = float(new_salary)
            return "Salary updated successfully"
    return "Employee not found"

# Delete employee
def delete_employee(emp_id):
    for emp in employee:
        if emp['id'] == emp_id:
            employee.remove(emp)
            return "Employee deleted successfully"
    return "Employee not found"                                                                                         