# =============================================================
# EXERCÍCIOS
# =============================================================

# Exercício 1:
# Crie variáveis para armazenar: seu nome, sua idade, sua altura
# e se você gosta de Python (True/False). Depois exiba tudo
# em uma única frase usando f-string.

nome = "Caio"
idade = 18
altura = 1.75
gosta_python = True

print(f"Meu nome é {nome}, tenho {idade} anos, "
      f"minha altura é {altura}m e gosto de Python: {gosta_python}")

# Exercício 2:
# Peça ao usuário para digitar um número com input(),
# converta para inteiro e exiba o dobro desse número.
# Dica: use int(input("Digite um número: "))

numero = int(input("Digite um número: "))

dobro = numero * 2

print(f"O dobro de {numero} é {dobro}")

# Exercício 3:
# Crie duas variáveis numéricas, troque os valores entre elas
# (sem usar uma terceira variável) e exiba o resultado.
# Dica: Python permite  a, b = b, a

a = 10
b = 20

print(f"Antes da troca: a = {a}, b = {b}")

a, b = b, a

print(f"Depois da troca: a = {a}, b = {b}")