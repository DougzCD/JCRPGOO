from supplier import Supplier
from employee import Employee
from administrator import Administrator

def main():
    while True:
        print("\nSistema de Gestão de Pessoas (SGP)")
        print("1. Adicionar Fornecedor")
        print("2. Adicionar Empregado")
        print("3. Adicionar Administrador")
        print("4. Sair")
        choice = input("Escolha uma opção: ")

        if choice == '1':
            try:
                nome = input("Nome: ")
                endereco = input("Endereço: ")
                cpf = input("CPF: ")
                rg = input("RG: ")
                telefone = input("Telefone: ")
                value_credit = float(input("Crédito: "))
                value_debt = float(input("Dívida: "))
                fornecedor = Supplier(nome, endereco, cpf, rg, telefone, value_credit, value_debt)
                print(f"Fornecedor {fornecedor.get_nome()} adicionado com sucesso.")
            except ValueError:
                print("Erro: Valor de crédito ou dívida inválido.")
            except Exception as e:
                print(f"Erro: {e}")

        elif choice == '2':
            try:
                nome = input("Nome: ")
                endereco = input("Endereço: ")
                cpf = input("CPF: ")
                rg = input("RG: ")
                telefone = input("Telefone: ")
                sector_code = int(input("Código do Setor: "))
                base_salary = float(input("Salário Base: "))
                tax = float(input("Imposto (%): "))
                empregado = Employee(nome, endereco, cpf, rg, telefone, sector_code, base_salary, tax)
                print(f"Empregado {empregado.get_nome()} adicionado com sucesso.")
                print(f"Salário calculado: {empregado.calculate_salary()}")
            except ValueError:
                print("Erro: Valor de salário ou imposto inválido.")
            except Exception as e:
                print(f"Erro: {e}")

        elif choice == '3':
            try:
                nome = input("Nome: ")
                endereco = input("Endereço: ")
                cpf = input("CPF: ")
                rg = input("RG: ")
                telefone = input("Telefone: ")
                sector_code = int(input("Código do Setor: "))
                base_salary = float(input("Salário Base: "))
                tax = float(input("Imposto (%): "))
                subsistence_allowance = float(input("Ajuda de Custo: "))
                administrador = Administrator(nome, endereco, cpf, rg, telefone, sector_code, base_salary, tax, subsistence_allowance)
                print(f"Administrador {administrador.get_nome()} adicionado com sucesso.")
                print(f"Salário calculado: {administrador.calculate_salary()}")
            except ValueError:
                print("Erro: Valor de salário, imposto ou ajuda de custo inválido.")
            except Exception as e:
                print(f"Erro: {e}")

        elif choice == '4':
            break

        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
