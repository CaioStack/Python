# =============================================================
# VARIÁVEIS E TIPOS DE DADOS EM PYTHON
# =============================================================
# Uma variável é um "apelido" para um espaço na memória onde
# guardamos um valor. Em Python, não precisamos declarar o tipo
# — ele é inferido automaticamente.

# -------------------------------------------------------------
# TIPOS BÁSICOS
# -------------------------------------------------------------

# int → números inteiros
idade = 25
ano = 2024
temperatura_negativa = -10

# float → números com casas decimais
altura = 1.75
preco = 99.90
pi = 3.14159

# str → texto (sempre entre aspas simples ou duplas)
nome = "Caio"
cidade = 'Fortaleza'
frase = "Python é incrível!"

# bool → verdadeiro ou falso
esta_chovendo = False
maior_de_idade = True

# NoneType → representa "nada" / ausência de valor
resultado = None

# -------------------------------------------------------------
# VERIFICANDO O TIPO DE UMA VARIÁVEL
# -------------------------------------------------------------
# A função type() retorna o tipo de qualquer valor.

print(type(idade))           # <class 'int'>
print(type(altura))          # <class 'float'>
print(type(nome))            # <class 'str'>
print(type(esta_chovendo))   # <class 'bool'>
print(type(resultado))       # <class 'NoneType'>

# -------------------------------------------------------------
# CONVERSÃO DE TIPOS (type casting)
# -------------------------------------------------------------
# Podemos converter um tipo em outro quando necessário.

numero_texto = "42"
numero_inteiro = int(numero_texto)   # str → int
numero_decimal = float(numero_texto) # str → float
texto_do_numero = str(123)           # int → str

print(numero_inteiro + 8)   # 50
print(numero_decimal + 0.5) # 42.5
print("Número: " + texto_do_numero)  # Número: 123

# -------------------------------------------------------------
# ATRIBUIÇÃO MÚLTIPLA
# -------------------------------------------------------------
# Python permite atribuir vários valores de uma vez.

x, y, z = 10, 20, 30
print(x, y, z)  # 10 20 30

# Todos com o mesmo valor
a = b = c = 0
print(a, b, c)  # 0 0 0

# -------------------------------------------------------------
# EXIBINDO VARIÁVEIS COM f-strings (forma moderna e recomendada)
# -------------------------------------------------------------
# Coloque f antes das aspas e use {} para inserir variáveis.

print(f"Olá, meu nome é {nome} e tenho {idade} anos.")
print(f"Minha altura é {altura}m e moro em {cidade}.")
print(f"O dobro da minha idade é {idade * 2}.")