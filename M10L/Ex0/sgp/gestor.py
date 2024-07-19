from .colaborador import Colaborador

class Gestor:
    def __init__(self):
        self.colaboradores = []

    def adicionar_colaborador(self):
        try:
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            cargo = input("Cargo: ")
            colaborador = Colaborador(nome, idade, cargo)
            self.colaboradores.append(colaborador)
            print("Colaborador adicionado com sucesso!")
        except ValueError:
            print("Erro: Idade deve ser um número inteiro.")

    def remover_colaborador(self):
        nome = input("Nome do colaborador a ser removido: ")
        colaborador = self.buscar_colaborador(nome)
        if colaborador:
            self.colaboradores.remove(colaborador)
            print("Colaborador removido com sucesso!")
        else:
            print("Colaborador não encontrado.")

    def atualizar_colaborador(self):
        nome = input("Nome do colaborador a ser atualizado: ")
        colaborador = self.buscar_colaborador(nome)
        if colaborador:
            try:
                nova_idade = int(input("Nova idade: "))
                novo_cargo = input("Novo cargo: ")
                colaborador.idade = nova_idade
                colaborador.cargo = novo_cargo
                print("Informações atualizadas com sucesso!")
            except ValueError:
                print("Erro: Idade deve ser um número inteiro.")
        else:
            print("Colaborador não encontrado.")

    def listar_colaboradores(self):
        if self.colaboradores:
            print("\n--- Lista de Colaboradores ---")
            for colaborador in self.colaboradores:
                print(colaborador)
        else:
            print("Nenhum colaborador cadastrado.")

    def buscar_colaborador(self, nome):
        for colaborador in self.colaboradores:
            if colaborador.nome == nome:
                return colaborador
        return None
