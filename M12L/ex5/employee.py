class Employee:
    def __init__(self, name, registration_number, salary):
        self.name = name
        self.registration_number = registration_number
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}")
        print(f"Registration Number: {self.registration_number}")
        print(f"Salary: {self.salary}")
