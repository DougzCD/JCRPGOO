from .person import Person

class Supplier(Person):
    def __init__(self, nome="", endereco="", cpf="", rg="", telefone="", value_credit=0.0, value_debt=0.0):
        super().__init__(nome, endereco, cpf, rg, telefone)
        self.__value_credit = value_credit
        self.__value_debt = value_debt

    # Getters
    def get_value_credit(self):
        return self.__value_credit

    def get_value_debt(self):
        return self.__value_debt

    def get_balance(self):
        return self.__value_credit - self.__value_debt

    # Setters
    def set_value_credit(self, value_credit):
        self.__value_credit = value_credit

    def set_value_debt(self, value_debt):
        self.__value_debt = value_debt

    def __str__(self):
        return (super().__str__() + 
                f", Crédito Máximo: {self.__value_credit}, Dívida: {self.__value_debt}, Saldo: {self.get_balance()}")
