from employee import Employee

class TechnicalAssistant(Employee):
    def __init__(self, name, registration_number, salary, bonus):
        super().__init__(name, registration_number, salary)
        self.bonus = bonus

    def display(self):
        super().display()
        print(f"Bonus: {self.bonus}")
        print(f"Total Salary: {self.salary + self.bonus}")
