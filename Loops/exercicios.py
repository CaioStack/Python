# =============================================================
# EXERCÍCIOS
# =============================================================

# Exercício 1:
# Exiba a tabuada de um número fornecido pelo usuário (de 1 a 10).

numero = int(input("Digite um número para ver a tabuada: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# Exercício 2:
# Calcule a soma de todos os números de 1 a 100 usando um loop.
# (Resposta esperada: 5050)

soma = 0

for i in range(1, 101):
    soma += i

print(f"A soma de 1 até 100 é {soma}")

# Exercício 3:
# Dada uma lista de números, crie uma nova lista apenas com
# os que são divisíveis por 3. Use list comprehension.

numeros = [3, 5, 9, 10, 12, 15, 18, 20]

divisiveis_por_3 = [n for n in numeros if n % 3 == 0]

print("Números divisíveis por 3:")
print(divisiveis_por_3)

# Exercício 4:
# Crie um programa que imprima um triângulo de asteriscos:
# *
# **
# ***
# ****
# *****

for i in range(1, 6):
    print("*" * i)