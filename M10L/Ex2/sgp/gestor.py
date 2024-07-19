from .colaborador import Colaborador
from .supplier import Supplier

class Gestor:
    def __init__(self):
        self.colaboradores = []
        self.fornecedores = []

    # Métodos para colaboradores (existentes)

    def adicionar_colaborador(self):
        try:
            nome = input("Nome: ")
            endereco = input("Endereço: ")
            cpf = input("CPF: ")
            rg = input("RG: ")
            telefone = input("Telefone: ")
            idade = int(input("Idade: "))
            cargo = input("Cargo: ")
            colaborador = Colaborador(nome, endereco, cpf, rg, telefone, idade, cargo)
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
                novo_endereco = input("Novo endereço: ")
                novo_cpf = input("Novo CPF: ")
                novo_rg = input("Novo RG: ")
                novo_telefone = input("Novo telefone: ")
                nova_idade = int(input("Nova idade: "))
                novo_cargo = input("Novo cargo: ")
                colaborador.set_endereco(novo_endereco)
                colaborador.set_cpf(novo_cpf)
                colaborador.set_rg(novo_rg)
                colaborador.set_telefone(novo_telefone)
                colaborador.set_idade(nova_idade)
                colaborador.set_cargo(novo_cargo)
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
            if colaborador.get_nome() == nome:
                return colaborador
        return None

    # Métodos para fornecedores

    def adicionar_fornecedor(self):
        try:
            nome = input("Nome: ")
            endereco = input("Endereço: ")
            cpf = input("CPF: ")
            rg = input("RG: ")
            telefone = input("Telefone: ")
            value_credit = float(input("Crédito Máximo: "))
            value_debt = float(input("Dívida: "))
            fornecedor = Supplier(nome, endereco, cpf, rg, telefone, value_credit, value_debt)
            self.fornecedores.append(fornecedor)
            print("Fornecedor adicionado com sucesso!")
        except ValueError:
            print("Erro: Valor de crédito ou dívida deve ser um número.")

    def remover_fornecedor(self):
        nome = input("Nome do fornecedor a ser removido: ")
        fornecedor = self.buscar_fornecedor(nome)
        if fornecedor:
            self.fornecedores.remove(fornecedor)
            print("Fornecedor removido com sucesso!")
        else:
            print("Fornecedor não encontrado.")

    def atualizar_fornecedor(self):
        nome = input("Nome do fornecedor a ser atualizado: ")
        fornecedor = self.buscar_fornecedor(nome)
        if fornecedor:
            try:
                novo_endereco = input("Novo endereço: ")
                novo_cpf = input("Novo CPF: ")
                novo_rg = input("Novo RG: ")
                novo_telefone = input("Novo telefone: ")
                novo_value_credit = float(input("Novo Crédito Máximo: "))
                novo_value_debt = float(input("Nova Dívida: "))
                fornecedor.set_endereco(novo_endereco)
                fornecedor.set_cpf(novo_cpf)
                fornecedor.set_rg(novo_rg)
                fornecedor.set_telefone(novo_telefone)
                fornecedor.set_value_credit(novo_value_credit)
                fornecedor.set_value_debt(novo_value_debt)
                print("Informações atualizadas com sucesso!")
            except ValueError:
                print("Erro: Valor de crédito ou dívida deve ser um número.")
        else:
            print("Fornecedor não encontrado.")

    def listar_fornecedores(self):
        if self.fornecedores:
            print("\n--- Lista de Fornecedores ---")
            for fornecedor in self.fornecedores:
                print(fornecedor)
        else:
            print("Nenhum fornecedor cadastrado.")

    def buscar_fornecedor(self, nome):
        for fornecedor in self.fornecedores:
            if fornecedor.get_nome() == nome:
                return fornecedor
        return None
