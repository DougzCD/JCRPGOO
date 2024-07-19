from .employee import Employee

class Administrator(Employee):
    def __init__(self, nome="", endereco="", cpf="", rg="", telefone="", sector_code=0, base_salary=0.0, tax=0.0, subsistence_allowance=0.0):
        super().__init__(nome, endereco, cpf, rg, telefone, sector_code, base_salary, tax)
        self.__subsistence_allowance = subsistence_allowance

    # Getter
    def get_subsistence_allowance(self):
        return self.__subsistence_allowance

    # Setter
    def set_subsistence_allowance(self, subsistence_allowance):
        self.__subsistence_allowance = subsistence_allowance

    def calculate_salary(self):
        return super().calculate_salary() + self.__subsistence_allowance

    def __str__(self):
        return (super().__str__() + 
                f", Ajuda de Custo: {self.__subsistence_allowance}, Salário com Ajuda de Custo: {self.calculate_salary()}")
