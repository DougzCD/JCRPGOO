class Colaborador:
    def __init__(self, nome, idade, cargo):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Cargo: {self.cargo}"
