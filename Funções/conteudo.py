# =============================================================
# FUNÇÕES
# =============================================================
# Uma função é um bloco de código reutilizável que realiza
# uma tarefa específica. Use funções para organizar o código,
# evitar repetição e facilitar manutenção.
# Definição: def nome_da_funcao(parametros):

# -------------------------------------------------------------
# FUNÇÃO SIMPLES (sem parâmetros, sem retorno)
# -------------------------------------------------------------

def saudacao():
    print("Olá! Bem-vindo ao Python!")

saudacao()  # chamando a função

# -------------------------------------------------------------
# FUNÇÃO COM PARÂMETROS
# -------------------------------------------------------------
# Parâmetros são variáveis que a função recebe para trabalhar.

def saudar_pessoa(nome):
    print(f"Olá, {nome}! Tudo bem?")

saudar_pessoa("Maria")
saudar_pessoa("João")

# -------------------------------------------------------------
# FUNÇÃO COM RETORNO (return)
# -------------------------------------------------------------
# O return envia um resultado de volta para quem chamou.
# Após o return, a função é encerrada.

def somar(a, b):
    resultado = a + b
    return resultado

total = somar(3, 7)
print(f"3 + 7 = {total}")
print(f"15 + 25 = {somar(15, 25)}")

# -------------------------------------------------------------
# PARÂMETROS COM VALOR PADRÃO
# -------------------------------------------------------------
# Se o argumento não for passado, usa o valor padrão.

def potencia(base, expoente=2):
    return base ** expoente

print(potencia(3))     # 9  (usa expoente=2 por padrão)
print(potencia(3, 3))  # 27 (usa expoente=3)
print(potencia(2, 10)) # 1024

# -------------------------------------------------------------
# ARGUMENTOS NOMEADOS (keyword arguments)
# -------------------------------------------------------------

def criar_perfil(nome, idade, cidade="Desconhecida"):
    print(f"Nome: {nome} | Idade: {idade} | Cidade: {cidade}")

criar_perfil("Ana", 25, "Fortaleza")
criar_perfil(idade=30, nome="Bruno")        # ordem não importa
criar_perfil("Carla", cidade="Recife", idade=22)

# -------------------------------------------------------------
# *args — número variável de argumentos posicionais
# -------------------------------------------------------------
# Recebe qualquer quantidade de argumentos como uma tupla.

def somar_tudo(*numeros):
    total = 0
    for n in numeros:
        total += n
    return total

print(somar_tudo(1, 2, 3))           # 6
print(somar_tudo(10, 20, 30, 40))    # 100

# -------------------------------------------------------------
# **kwargs — número variável de argumentos nomeados
# -------------------------------------------------------------
# Recebe argumentos nomeados como um dicionário.

def exibir_dados(**dados):
    for chave, valor in dados.items():
        print(f"  {chave}: {valor}")

exibir_dados(nome="Bia", profissao="Dev", linguagem="Python")

# -------------------------------------------------------------
# RETORNANDO MÚLTIPLOS VALORES
# -------------------------------------------------------------
# Python permite retornar vários valores como uma tupla.

def minmax(lista):
    return min(lista), max(lista)

minimo, maximo = minmax([5, 2, 8, 1, 9, 3])
print(f"Mínimo: {minimo}, Máximo: {maximo}")

# -------------------------------------------------------------
# FUNÇÕES LAMBDA (funções anônimas de uma linha)
# -------------------------------------------------------------
# Úteis para operações simples e rápidas.
# Sintaxe: lambda parâmetros: expressão

dobro = lambda x: x * 2
quadrado = lambda x: x ** 2
soma = lambda a, b: a + b

print(dobro(5))      # 10
print(quadrado(4))   # 16
print(soma(3, 7))    # 10

# Muito usadas com sorted(), map(), filter()
numeros = [5, 2, 8, 1, 9, 3]
print(sorted(numeros, reverse=True))           # [9, 8, 5, 3, 2, 1]

pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 8]

dobros = list(map(lambda x: x * 2, numeros))
print(dobros) # [10, 4, 16, 2, 18, 6]

# -------------------------------------------------------------
# ESCOPO DE VARIÁVEIS
# -------------------------------------------------------------
# Variáveis criadas dentro de funções são locais (não existem fora).
# Variáveis fora das funções são globais.

total_global = 100  # variável global

def minha_funcao():
    total_local = 50   # variável local
    print(f"Dentro: global={total_global}, local={total_local}")

minha_funcao()
print(f"Fora: global={total_global}")
# print(total_local)  # ERRO! total_local não existe aqui