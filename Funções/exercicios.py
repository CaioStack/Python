# =============================================================
# EXERCÍCIOS
# =============================================================

# Exercício 1:
# Crie uma função que receba uma temperatura em Celsius
# e retorne em Fahrenheit. Fórmula: F = C * 9/5 + 32

def celsius_para_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

temp = 30

print(f"{temp}°C = {celsius_para_fahrenheit(temp)}°F")

# Exercício 2:
# Crie uma função que receba uma lista de notas e retorne
# a média. Teste com [7, 8, 9, 6, 10].

def calcular_media(notas):
    media = sum(notas) / len(notas)
    return media

lista_notas = [7, 8, 9, 6, 10]

print(f"Média das notas: {calcular_media(lista_notas):.2f}")

# Exercício 3:
# Crie uma função is_palindromo(palavra) que retorne True
# se a palavra é um palíndromo (lida igual de trás pra frente).
# Teste: "arara" → True, "python" → False
# Dica: palavra == palavra[::-1]

def is_palindromo(palavra):
    return palavra == palavra[::-1]

print(is_palindromo("arara"))   # True
print(is_palindromo("python"))  # False

# Exercício 4:
# Usando lambda e filter(), filtre apenas os números
# maiores que 10 da lista [3, 15, 7, 22, 8, 11, 1, 30].

numeros = [3, 15, 7, 22, 8, 11, 1, 30]

maiores_que_10 = list(filter(lambda x: x > 10, numeros))

print(maiores_que_10)