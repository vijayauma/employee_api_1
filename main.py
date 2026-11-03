
from fastapi import FastAPI
from pydantic import BaseModel, Field

# Create FastAPI application
app = FastAPI(title="Employee Management API")

# Sample employee data
employees = [
    {
        "id": 101,
        "name": "Rahul",
        "department": "IT",
        "age": 25,
        "salary": 35000
    },
    {
        "id": 102,
        "name": "Priya",
        "department": "HR",
        "age": 28,
        "salary": 40000
    },
    {
        "id": 103,
        "name": "Arun",
        "department": "IT",
        "age": 30,
        "salary": 45000
    }
]


# Pydantic model for employee registration
class Employee(BaseModel):
    id: int
    name: str = Field(min_length=3)
    department: str
    age: int = Field(gt=18, lt=60)
    salary: float = Field(gt=0)


# 1. Home API
@app.get("/")
def home():
    return {"message": "Welcome to Employee Management API"}


# 2. Get all employees
@app.get("/employees")
def get_employees():
    return employees


# 3. Get employee using path parameter
@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):

    for employee in employees:
        if employee["id"] == employee_id:
            return employee

    return {"message": "Employee not found"}


# 4. Filter employees using query parameter
@app.get("/filter-employees")
def filter_employees(department: str):

    result = []

    for employee in employees:
        if employee["department"].lower() == department.lower():
            result.append(employee)

    return result


# 5. Register a new employee using POST
@app.post("/employees")
def add_employee(employee: Employee):

    employees.append(employee.model_dump())

    return {
        "message": "Employee registered successfully",
        "employee": employee
    }
