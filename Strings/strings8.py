# Leia o nome completo de uma pessoa e mostre:
# - O nome todo em letras maiúsculas
# - O nome todo em letras minúsculas
# - A quantidade total de caracteres, sem contar espaços
# - A primeira letra do nome

# Solicita o nome completo do usuário
nome_completo = input("Digite seu nome completo: ")

# 1. Nome todo em letras maiúsculas
print(f"Maiúsculas: {nome_completo.upper()}")

# 2. Nome todo em letras minúsculas
print(f"Minúsculas: {nome_completo.lower()}")

# 3. Quantidade total de caracteres (sem contar espaços)
# O método replace(" ", "") remove todos os espaços em branco
total_caracteres = len(nome_completo.replace(" ", ""))
print(f"Total de letras: {total_caracteres}")

# 4. A primeira letra do nome todo
# O método strip() remove espaços extras no início/fim para evitar erros
primeira_letra = nome_completo.strip()[0]
print(f"Primeira letra: {primeira_letra}")