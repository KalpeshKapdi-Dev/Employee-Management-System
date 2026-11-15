class Employee:

    def __init__(self, employee_id, name, age, email, department, salary):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.email = email
        self.department = department
        self.salary = salary

    def to_dict(self):
        return {
            "employee_id": self.employee_id,
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "department": self.department,
            "salary": self.salary
        }