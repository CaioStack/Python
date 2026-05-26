# Crie um programa que:
# - Leia 6 números inteiros
# - Armazene os números em uma lista
# - Depois leia um número de busca
# - Informe se esse número aparece ou não na lista

numeros4 = []

for i in range(6):
    numero = int(input(f"Digite o número {i + 1}: "))
    numeros4.append(numero)

busca = int(input("Digite o número que deseja buscar: "))

encontrado = False
for i in range(len(numeros4)):
    if numeros4[i] == busca:
        encontrado = True

if encontrado:
    print(f"O número {busca} FOI encontrado na lista.")
else:
    print(f"O número {busca} NÃO foi encontrado na lista.")