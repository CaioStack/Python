# =============================================================
# EXERCÍCIOS
# =============================================================

# Exercício 1:
# Peça ao usuário um texto e exiba:
# a) O texto em maiúsculas
# b) Quantas letras tem (sem contar espaços)
# c) O texto invertido

texto = input("Digite um texto: ")

# a) Texto em maiúsculas
print("Maiúsculas:", texto.upper())

# b) Quantidade de letras sem espaços
quantidade = len(texto.replace(" ", ""))
print("Quantidade de letras:", quantidade)

# c) Texto invertido
print("Texto invertido:", texto[::-1])

# Exercício 2:
# Dado o e-mail "usuario@exemplo.com.br", extraia
# apenas o nome de usuário (antes do @) e o domínio (depois do @).

email = "usuario@exemplo.com.br"

usuario, dominio = email.split("@")

print("Usuário:", usuario)
print("Domínio:", dominio)

# Exercício 3:
# Crie uma função que receba uma frase e retorne ela
# com a primeira letra de cada palavra em maiúscula,
# mas sem usar o método .title(). Use .split() e .join().

def capitalizar_frase(frase):
    palavras = frase.split()

    palavras_formatadas = []

    for palavra in palavras:
        nova_palavra = palavra[0].upper() + palavra[1:]
        palavras_formatadas.append(nova_palavra)

    return " ".join(palavras_formatadas)


frase = "python é muito legal"

print(capitalizar_frase(frase))

# Exercício 4:
# Verifique se a string "racecar" é um palíndromo
# usando fatiamento. Exiba uma mensagem explicando o resultado.

palavra = "racecar"

if palavra == palavra[::-1]:
    print(f'"{palavra}" é um palíndromo.')
else:
    print(f'"{palavra}" não é um palíndromo.')