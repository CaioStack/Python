# Crie um programa que:
# - Leia 5 números inteiros
# - Armazene os números em uma lista
# - Mostre:
#   - o maior número
#   - o índice onde ele está

numeros2 = []

for i in range(5):
    numero = int(input(f"Digite o número {i + 1}: "))
    numeros2.append(numero)

maior = numeros2[0]
indice_maior = 0

for i in range(1, len(numeros2)):
    if numeros2[i] > maior:
        maior = numeros2[i]
        indice_maior = i

print(f"O maior número é: {maior}")
print(f"Ele está no índice: {indice_maior}")