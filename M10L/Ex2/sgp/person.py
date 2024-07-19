class Person:
    def __init__(self, nome="", endereco="", cpf="", rg="", telefone=""):
        self.__nome = nome
        self.__endereco = endereco
        self.__cpf = cpf
        self.__rg = rg
        self.__telefone = telefone

    # Getters
    def get_nome(self):
        return self.__nome

    def get_endereco(self):
        return self.__endereco

    def get_cpf(self):
        return self.__cpf

    def get_rg(self):
        return self.__rg

    def get_telefone(self):
        return self.__telefone

    # Setters
    def set_nome(self, nome):
        self.__nome = nome

    def set_endereco(self, endereco):
        self.__endereco = endereco

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def set_rg(self, rg):
        self.__rg = rg

    def set_telefone(self, telefone):
        self.__telefone = telefone

    def __str__(self):
        return (f"Nome: {self.__nome}, Endereço: {self.__endereco}, CPF: {self.__cpf}, "
                f"RG: {self.__rg}, Telefone: {self.__telefone}")
