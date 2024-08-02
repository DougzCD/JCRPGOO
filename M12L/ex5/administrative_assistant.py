from employee import Employee

class AdministrativeAssistant(Employee):
    def __init__(self, name, registration_number, salary, shift, night_additional):
        super().__init__(name, registration_number, salary)
        self.shift = shift
        self.night_additional = night_additional

    def display(self):
        super().display()
        print(f"Shift: {self.shift}")
        if self.shift.lower() == 'night':
            print(f"Night Additional: {self.night_additional}")
