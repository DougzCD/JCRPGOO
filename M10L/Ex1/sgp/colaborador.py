from .pessoa import Pessoa

class Colaborador(Pessoa):
    def __init__(self, nome="", endereco="", cpf="", rg="", telefone="", idade=0, cargo=""):
        super().__init__(nome, endereco, cpf, rg, telefone)
        self.__idade = idade
        self.__cargo = cargo

    # Getters
    def get_idade(self):
        return self.__idade

    def get_cargo(self):
        return self.__cargo

    # Setters
    def set_idade(self, idade):
        self.__idade = idade

    def set_cargo(self, cargo):
        self.__cargo = cargo

    def __str__(self):
        return (super().__str__() + 
                f", Idade: {self.__idade}, Cargo: {self.__cargo}")
