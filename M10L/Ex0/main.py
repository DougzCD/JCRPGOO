from sgp.gestor import Gestor

def menu():
    print("\n--- Sistema de Gestão de Pessoas (SGP) ---")
    print("1. Adicionar colaborador")
    print("2. Remover colaborador")
    print("3. Atualizar informações do colaborador")
    print("4. Listar colaboradores")
    print("5. Sair")
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
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
