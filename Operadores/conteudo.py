# =============================================================
# OPERADORES EM PYTHON
# =============================================================
# Operadores são símbolos que realizam operações sobre valores.

# -------------------------------------------------------------
# OPERADORES ARITMÉTICOS
# -------------------------------------------------------------

a = 10
b = 3

print(a + b)   # 13  → adição
print(a - b)   # 7   → subtração
print(a * b)   # 30  → multiplicação
print(a / b)   # 3.333... → divisão (sempre retorna float)
print(a // b)  # 3   → divisão inteira (descarta o resto)
print(a % b)   # 1   → módulo (resto da divisão)
print(a ** b)  # 1000 → potenciação (10³)

# -------------------------------------------------------------
# OPERADORES DE COMPARAÇÃO
# -------------------------------------------------------------
# Sempre retornam True ou False.

x = 5
y = 8

print(x == y)   # False → igual a
print(x != y)   # True  → diferente de
print(x > y)    # False → maior que
print(x < y)    # True  → menor que
print(x >= 5)   # True  → maior ou igual
print(x <= 4)   # False → menor ou igual

# -------------------------------------------------------------
# OPERADORES LÓGICOS
# -------------------------------------------------------------
# Combinam expressões booleanas.

# and → True somente se AMBOS forem True
print(True and True)   # True
print(True and False)  # False

# or → True se PELO MENOS UM for True
print(True or False)   # True
print(False or False)  # False

# not → inverte o valor
print(not True)   # False
print(not False)  # True

# Exemplo prático:
idade = 20
tem_carteira = True

pode_dirigir = idade >= 18 and tem_carteira
print(f"Pode dirigir? {pode_dirigir}")  # True

# -------------------------------------------------------------
# OPERADORES DE ATRIBUIÇÃO
# -------------------------------------------------------------
# Formas abreviadas de atualizar variáveis.

n = 10
n += 5   # equivale a n = n + 5  → 15
n -= 3   # equivale a n = n - 3  → 12
n *= 2   # equivale a n = n * 2  → 24
n //= 4  # equivale a n = n // 4 → 6
n **= 2  # equivale a n = n ** 2 → 36
print(n) # 36

# -------------------------------------------------------------
# PRECEDÊNCIA DE OPERADORES
# -------------------------------------------------------------
# A ordem de execução segue a matemática: ** > * / // % > + -
# Use parênteses para garantir a ordem desejada.

print(2 + 3 * 4)    # 14  (multiplicação primeiro)
print((2 + 3) * 4)  # 20  (parênteses primeiro)
print(2 ** 3 + 1)   # 9   (potência antes da soma)