import json
import os

from models.employee import Employee


class EmployeeService:

    def __init__(self):
        self.file_path = "data/employees.json"

        # Create file if it doesn't exist
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as file:
                json.dump([], file, indent=4)

    # Read employees from JSON file
    def read_data(self):

        with open(self.file_path, "r") as file:
            return json.load(file)

    # Write employees to JSON file
    def write_data(self, employees):

        with open(self.file_path, "w") as file:
            json.dump(employees, file, indent=4)

    # Add employee
    def add_employee(self, employee):

        employees = self.read_data()

        employees.append(employee.to_dict())

        self.write_data(employees)

        print("Employee added successfully.")

    # View all employees
    def get_all_employees(self):

        employees = self.read_data()

        if len(employees) == 0:
            print("No employees found.")
            return

        for employee in employees:

            print("--------------------------------")
            print("Employee ID :", employee["employee_id"])
            print("Name        :", employee["name"])
            print("Age         :", employee["age"])
            print("Email       :", employee["email"])
            print("Department  :", employee["department"])
            print("Salary      :", employee["salary"])

    # Search employee
    def search_employee(self, employee_id):

        employees = self.read_data()

        for employee in employees:

            if employee["employee_id"] == employee_id:

                print("--------------------------------")
                print("Employee ID :", employee["employee_id"])
                print("Name        :", employee["name"])
                print("Age         :", employee["age"])
                print("Email       :", employee["email"])
                print("Department  :", employee["department"])
                print("Salary      :", employee["salary"])

                return

        print("Employee not found.")

    # Update employee
    def update_employee(self, employee_id):

        employees = self.read_data()

        for employee in employees:

            if employee["employee_id"] == employee_id:

                print("Employee found.")

                employee["name"] = input("Enter new name: ")
                employee["age"] = int(input("Enter new age: "))
                employee["email"] = input("Enter new email: ")
                employee["department"] = input("Enter new department: ")
                employee["salary"] = float(input("Enter new salary: "))

                self.write_data(employees)

                print("Employee updated successfully.")

                return

        print("Employee not found.")

    # Delete employee
    def delete_employee(self, employee_id):

        employees = self.read_data()

        for employee in employees:

            if employee["employee_id"] == employee_id:

                employees.remove(employee)

                self.write_data(employees)

                print("Employee deleted successfully.")

                return

        print("Employee not found.")