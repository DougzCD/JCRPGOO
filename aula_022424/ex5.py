# Programa para cálculo do novo salário dos funcionários da empresa XYZ
SALARIO_LIMITE = 2000
PERCENTUAL_AUMENTO = 0.3
# Apresentacao do programa
print("++++++++++++++++++++++++++++++++++++++\n")
print("Calculo do Novo Salario da Empresa XYZ \n")
print("++++++++++++++++++++++++++++++++++++++\n\n")
# Leitura do salário
salario = float(input("Digite seu salário: "))
# Verificação se o usuário digitou um valor válido para salário 
if salario <= 0:
    print("Voce digitou um salario invalido!\n")
elif salario >= SALARIO_LIMITE:
    print("Voce ficarah com o mesmo salario. \n")
else:
    salario = salario + salario*PERCENTUAL_AUMENTO;
    print(f"Novo salário: R$ {salario:,.2f}")