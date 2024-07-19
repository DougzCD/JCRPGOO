from .colaborador import Colaborador
from .supplier import Supplier
from .employee import Employee

class Gestor:
    def __init__(self):
        self.colaboradores = []
        self.fornecedores = []
        self.empregados = []

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

    # Métodos para empregados

    def adicionar_empregado(self):
        try:
            nome = input("Nome: ")
            endereco = input("Endereço: ")
            cpf = input("CPF: ")
            rg = input("RG: ")
            telefone = input("Telefone: ")
            sector_code = int(input("Código do Setor: "))
            base_salary = float(input("Salário Base: "))
            tax = float(input("Impostos (%): "))
            empregado = Employee(nome, endereco, cpf, rg, telefone, sector_code, base_salary, tax)
            self.empregados.append(empregado)
            print("Empregado adicionado com sucesso!")
        except ValueError:
            print("Erro: Código do setor deve ser um número inteiro e valores de salário e impostos devem ser números.")

    def remover_empregado(self):
        nome = input("Nome do empregado a ser removido: ")
        empregado = self.buscar_empregado(nome)
        if empregado:
            self.empregados.remove(empregado)
            print("Empregado removido com sucesso!")
        else:
            print("Empregado não encontrado.")

    def atualizar_empregado(self):
        nome = input("Nome do empregado a ser atualizado: ")
        empregado = self.buscar_empregado(nome)
        if empregado:
            try:
                novo_endereco = input("Novo endereço: ")
                novo_cpf = input("Novo CPF: ")
                novo_rg = input("Novo RG: ")
                novo_telefone = input("Novo telefone: ")
                novo_sector_code = int(input("Novo Código do Setor: "))
                novo_base_salary = float(input("Novo Salário Base: "))
                novo_tax = float(input("Novos Impostos (%): "))
                empregado.set_endereco(novo_endereco)
                empregado.set_cpf(novo_cpf)
                empregado.set_rg(novo_rg)
                empregado.set_telefone(novo_telefone)
                empregado.set_sector_code(novo_sector_code)
                empregado.set_base_salary(novo_base_salary)
                empregado.set_tax(novo_tax)
                print("Informações atualizadas com sucesso!")
            except ValueError:
                print("Erro: Código do setor deve ser um número inteiro e valores de salário e impostos devem ser números.")
        else:
            print("Empregado não encontrado.")

    def listar_empregados(self):
        if self.empregados:
            print("\n--- Lista de Empregados ---")
            for empregado in self.empregados:
                print(empregado)
        else:
            print("Nenhum empregado cadastrado.")

    def buscar_empregado(self, nome):
        for empregado in self.empregados:
            if empregado.get_nome() == nome:
                return empregado
        return None
