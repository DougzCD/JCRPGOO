from .person import Person

class Employee(Person):
    def __init__(self, nome="", endereco="", cpf="", rg="", telefone="", sector_code=0, base_salary=0.0, tax=0.0):
        super().__init__(nome, endereco, cpf, rg, telefone)
        self.__sector_code = sector_code
        self.__base_salary = base_salary
        self.__tax = tax

    # Getters
    def get_sector_code(self):
        return self.__sector_code

    def get_base_salary(self):
        return self.__base_salary

    def get_tax(self):
        return self.__tax

    # Setters
    def set_sector_code(self, sector_code):
        self.__sector_code = sector_code

    def set_base_salary(self, base_salary):
        self.__base_salary = base_salary

    def set_tax(self, tax):
        self.__tax = tax

    def calculate_salary(self):
        return self.__base_salary * (1 - self.__tax / 100)

    def __str__(self):
        return (super().__str__() + 
                f", Código do Setor: {self.__sector_code}, Salário Base: {self.__base_salary}, Impostos: {self.__tax}%, Salário Líquido: {self.calculate_salary()}")
