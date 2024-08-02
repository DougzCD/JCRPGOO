from employee import Employee

class Administrator(Employee):
    def __init__(self, nome, endereco, cpf, rg, telefone, sector_code, base_salary, tax, subsistence_allowance):
        super().__init__(nome, endereco, cpf, rg, telefone, sector_code, base_salary, tax)
        self.__subsistence_allowance = subsistence_allowance

    # Getters
    def get_subsistence_allowance(self):
        return self.__subsistence_allowance

    # Setters
    def set_subsistence_allowance(self, subsistence_allowance):
        self.__subsistence_allowance = subsistence_allowance

    def calculate_salary(self):
        base_salary = super().calculate_salary()
        return base_salary + self.__subsistence_allowance
