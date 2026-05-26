# Crie um programa que:
# - Leia 5 números inteiros
# - Armazene os números em uma lista
# - Mostre o maior número da lista

numeros = []

for i in range(5):
    numero = int(input(f"Digite o número {i + 1}: "))
    numeros.append(numero)

maior = numeros[0]
for i in range(1, len(numeros)):
    if numeros[i] > maior:
        maior = numeros[i]

print(f"O maior número é: {maior}")