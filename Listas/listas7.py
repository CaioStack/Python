# Crie um programa que:
# - Leia 8 números inteiros
# - Armazene os números em uma lista
# - Mostre quantos números pares existem na lista

numeros3 = []

for i in range(8):
    numero = int(input(f"Digite o número {i + 1}: "))
    numeros3.append(numero)

qtd_pares = 0
for i in range(len(numeros3)):
    if numeros3[i] % 2 == 0:
        qtd_pares = qtd_pares + 1

print(f"Quantidade de números pares: {qtd_pares}")