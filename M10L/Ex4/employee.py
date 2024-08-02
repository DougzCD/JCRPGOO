from person import Person

class Employee(Person):
    def __init__(self, nome, endereco, cpf, rg, telefone, sector_code, base_salary, tax):
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
