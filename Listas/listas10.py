# Crie uma função chamada contar_pares.
# A função deve:
# - Receber uma lista de números
# - Contar quantos números pares existem
# - Retornar essa quantidade
# Depois:
# - Leia 6 números inteiros
# - Armazene os números em uma lista
# - Chame a função
# - Mostre o resultado

def contar_pares(lista):
    quantidade = 0
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            quantidade = quantidade + 1
    return quantidade

numeros5 = []

for i in range(6):
    numero = int(input(f"Digite o número {i + 1}: "))
    numeros5.append(numero)

resultado = contar_pares(numeros5)

print(f"Quantidade de números pares na lista: {resultado}")