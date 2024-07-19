from sgp.gestor import Gestor

def menu():
    print("\n--- Sistema de Gestão de Pessoas (SGP) ---")
    print("1. Adicionar colaborador")
    print("2. Remover colaborador")
    print("3. Atualizar informações do colaborador")
    print("4. Listar colaboradores")
    print("5. Adicionar fornecedor")
    print("6. Remover fornecedor")
    print("7. Atualizar informações do fornecedor")
    print("8. Listar fornecedores")
    print("9. Adicionar empregado")
    print("10. Remover empregado")
    print("11. Atualizar informações do empregado")
    print("12. Listar empregados")
    print("13. Adicionar administrador")
    print("14. Remover administrador")
    print("15. Atualizar informações do administrador")
    print("16. Listar administradores")
    print("17. Sair")
    return input("Escolha uma opção: ")

def main():
    gestor = Gestor()
    
    while True:
        opcao = menu()
        if opcao == '1':
            gestor.adicionar_colaborador()
        elif opcao == '2':
            gestor.remover_colaborador()
        elif opcao == '3':
            gestor.atualizar_colaborador()
        elif opcao == '4':
            gestor.listar_colaboradores()
        elif opcao == '5':
            gestor.adicionar_fornecedor()
        elif opcao == '6':
            gestor.remover_fornecedor()
        elif opcao == '7':
            gestor.atualizar_fornecedor()
        elif opcao == '8':
            gestor.listar_fornecedores()
        elif opcao == '9':
            gestor.adicionar_empregado()
        elif opcao == '10':
            gestor.remover_empregado()
        elif opcao == '11':
            gestor.atualizar_empregado()
        elif opcao == '12':
            gestor.listar_empregados()
        elif opcao == '13':
            gestor.adicionar_administrador()
        elif opcao == '14':
            gestor.remover_administrador()
        elif opcao == '15':
            gestor.atualizar_administrador()
        elif opcao == '16':
            gestor.listar_administradores()
        elif opcao == '17':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
