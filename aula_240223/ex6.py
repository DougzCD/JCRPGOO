numero = -1
while numero <= 0:
    numero = int(input("Digite um número positivo: "))
    if numero <= 0:
        print('\tVocê precisa digitar um número positivo!\n')
menor = numero # o primeiro número é utilizado como referência
while numero > 0:
    numero = int(input("Digite um número positivo: "))
 
    if numero < menor and numero > 0:
        menor = numero
print(f"Menor número: {menor}")