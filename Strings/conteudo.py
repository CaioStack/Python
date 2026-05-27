# =============================================================
# STRINGS — MANIPULAÇÃO DE TEXTO
# =============================================================
# Strings são sequências de caracteres. Em Python, elas são
# imutáveis: não podemos alterar caracteres diretamente,
# mas podemos criar novas strings a partir delas.

# -------------------------------------------------------------
# CRIANDO STRINGS
# -------------------------------------------------------------

simples = 'Olá, mundo!'
duplas = "Python é incrível!"
multilinhas = """Este texto
ocupa várias
linhas."""

print(simples)
print(duplas)
print(multilinhas)

# -------------------------------------------------------------
# INDEXAÇÃO E FATIAMENTO (slicing)
# -------------------------------------------------------------
# Strings são indexadas a partir do 0.
# Índices negativos contam do fim: -1 é o último caractere.

palavra = "Python"
#           P  y  t  h  o  n
# índice:   0  1  2  3  4  5
# negativo:-6 -5 -4 -3 -2 -1

print(palavra[0])    # P (primeiro)
print(palavra[-1])   # n (último)
print(palavra[2])    # t

# Fatiamento: string[início:fim:passo]
print(palavra[0:3])  # Pyt  (do índice 0 até 2)
print(palavra[2:])   # thon (do índice 2 até o fim)
print(palavra[:4])   # Pyth (do início até o índice 3)
print(palavra[::-1]) # nohtyP (invertida!)

# -------------------------------------------------------------
# MÉTODOS ESSENCIAIS DE STRING
# -------------------------------------------------------------

texto = "  Olá, Mundo! Python é Fantástico!  "

# Maiúsculas e minúsculas
print(texto.upper())       # TUDO EM MAIÚSCULAS
print(texto.lower())       # tudo em minúsculas
print(texto.title())       # Primeira Letra De Cada Palavra
print(texto.capitalize())  # Só a primeira letra maiúscula

# Remover espaços
print(texto.strip())       # remove espaços dos dois lados
print(texto.lstrip())      # remove espaços à esquerda
print(texto.rstrip())      # remove espaços à direita

# Verificações (retornam True/False)
print("python123".isalpha())   # False (tem números)
print("python".isalpha())      # True (só letras)
print("123".isdigit())         # True (só dígitos)
print("python".startswith("py"))  # True
print("python".endswith("on"))    # True

# Busca e contagem
frase = "banana é uma fruta, banana é gostosa"
print(frase.count("banana"))     # 2
print(frase.find("fruta"))       # 16 (índice da primeira ocorrência)
print(frase.find("manga"))       # -1 (não encontrado)
print("fruta" in frase)          # True

# Substituição
print(frase.replace("banana", "manga"))

# Dividir e juntar
csv = "Ana,Bruno,Carla,Diego"
lista = csv.split(",")          # divide: ['Ana', 'Bruno', 'Carla', 'Diego']
print(lista)

juntado = " | ".join(lista)     # junta: 'Ana | Bruno | Carla | Diego'
print(juntado)

# -------------------------------------------------------------
# FORMATAÇÃO DE STRINGS
# -------------------------------------------------------------

nome = "Maria"
idade = 25
altura = 1.68

# f-string (moderna e recomendada — Python 3.6+)
print(f"Nome: {nome}, Idade: {idade}, Altura: {altura}")
print(f"Altura com 1 decimal: {altura:.1f}")
print(f"Número alinhado: {idade:>5}")   # alinha à direita em 5 chars
print(f"Com zeros: {42:05d}")           # 00042

# .format() (ainda muito usada)
print("Nome: {}, Idade: {}".format(nome, idade))
print("Nome: {nome}, Idade: {idade}".format(nome=nome, idade=idade))

# % (estilo antigo, ainda encontrado em código legado)
print("Nome: %s, Idade: %d" % (nome, idade))

# -------------------------------------------------------------
# CARACTERES ESPECIAIS (escape sequences)
# -------------------------------------------------------------

print("Linha 1\nLinha 2")          # \n → nova linha
print("Col1\tCol2\tCol3")          # \t → tabulação
print("Ele disse \"olá\"")         # \" → aspas dentro de string
print("Barra: C:\\Users\\nome")    # \\ → barra invertida literal

# raw string: ignora os escape sequences
print(r"C:\Users\nome")  # imprime literalmente