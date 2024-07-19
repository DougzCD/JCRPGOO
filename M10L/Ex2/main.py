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
    print("9. Sair")
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
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
