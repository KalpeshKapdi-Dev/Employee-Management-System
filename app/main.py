from models.employee import Employee
from services.employee_service import EmployeeService


def DisplayMenu():

    print("\n================================")
    print("   EMPLOYEE MANAGEMENT SYSTEM")
    print("================================")

    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")

service = EmployeeService()

while True:

    DisplayMenu()

    choice = int(input("\nPlease Enter Your Choice : "));

    # Add Employees
    if choice == 1:
         
        employee_id = int(input("\nPlease Enter Employee ID: "))
        name = input("\nPlease Enter Name: ")
        age = int(input("\nPlease Enter Age: "))
        email = input("\nPlease Enter Email: ")
        department = input("\nPlease Enter Department: ")
        salary = float(input("\nPlease Enter Salary: "))

        employee = Employee(
            employee_id,
            name,
            age,
            email,
            department,
            salary
        )
        
        service.add_employee(employee)

        # View Employees
    elif choice == 2:

        service.get_all_employees()

    # Search Employee
    elif choice == 3:

        employee_id = int(input("Enter Employee ID: "))

        service.search_employee(employee_id)

    # Update Employee
    elif choice == 4:

        employee_id = int(input("Enter Employee ID: "))

        service.update_employee(employee_id)

    # Delete Employee
    elif choice == 5:

        employee_id = int(input("Enter Employee ID: "))

        service.delete_employee(employee_id)

    elif choice == 6:
        print("\nThank You.........")
        break

    else:

        print("\nInvalid choice. Please try again.")
