# =============================================================
# LISTAS, TUPLAS E SETS (CONJUNTOS)
# =============================================================

# =============================================================
# LISTAS — coleção ordenada e mutável
# =============================================================
# Listas aceitam qualquer tipo de dado e permitem duplicatas.
# Definidas com colchetes [].

# Criando listas
frutas = ["maçã", "banana", "laranja"]
numeros = [1, 2, 3, 4, 5]
mista = [1, "texto", 3.14, True, None]
vazia = []
lista_de_listas = [[1, 2], [3, 4], [5, 6]]

# ── Acessando elementos ──
print(frutas[0])    # maçã (primeiro)
print(frutas[-1])   # laranja (último)
print(frutas[1:3])  # ['banana', 'laranja'] (fatiamento)

# ── Modificando elementos ──
frutas[1] = "uva"
print(frutas)  # ['maçã', 'uva', 'laranja']

# ── Métodos principais ──
frutas.append("manga")        # adiciona no final
frutas.insert(1, "kiwi")      # insere no índice 1
frutas.extend(["abacaxi", "melão"])  # adiciona vários

print(frutas)

frutas.remove("kiwi")    # remove pelo valor
removido = frutas.pop()  # remove e retorna o último
removido2 = frutas.pop(0)  # remove e retorna pelo índice
print(f"Removidos: {removido}, {removido2}")

# ── Busca e informações ──
numeros = [3, 1, 4, 1, 5, 9, 2, 6]
print(len(numeros))          # 8 → tamanho
print(numeros.count(1))      # 2 → quantas vezes 1 aparece
print(numeros.index(4))      # 2 → índice do valor 4
print(4 in numeros)          # True

# ── Ordenação ──
numeros.sort()                    # ordena a lista original (in-place)
print(numeros)                    # [1, 1, 2, 3, 4, 5, 6, 9]

numeros.sort(reverse=True)        # ordem decrescente
print(numeros)

nova = sorted([5, 2, 8, 1])      # retorna nova lista (não modifica a original)
print(nova)

numeros.reverse()                 # inverte a ordem
palavras = ["banana", "maçã", "kiwi"]
palavras.sort(key=len)            # ordena por tamanho
print(palavras)

# ── Copiando listas ──
# CUIDADO: lista2 = lista1 não copia! Ambas apontam para o mesmo objeto.
original = [1, 2, 3]
copia_errada = original         # NÃO é uma cópia real!
copia_correta = original.copy() # ou: original[:]  ou list(original)

copia_errada.append(99)
print(original)       # [1, 2, 3, 99] ← foi modificado!
print(copia_correta)  # [1, 2, 3] ← não foi afetado

# =============================================================
# TUPLAS — coleção ordenada e IMUTÁVEL
# =============================================================
# Definidas com parênteses (). Não podem ser modificadas após
# a criação. Usadas para dados que não devem mudar.

coordenadas = (10.5, -3.7)
rgb_vermelho = (255, 0, 0)
dias_uteis = ("seg", "ter", "qua", "qui", "sex")

# Acessando (igual às listas)
print(coordenadas[0])   # 10.5
print(dias_uteis[1:4])  # ('ter', 'qua', 'qui')

# Desempacotamento de tuplas
x, y = coordenadas
print(f"x={x}, y={y}")

r, g, b = rgb_vermelho
print(f"R={r}, G={g}, B={b}")

# Tuplas são mais rápidas e seguras que listas para dados fixos
print(len(dias_uteis))             # 5
print("sex" in dias_uteis)         # True
print(dias_uteis.count("seg"))     # 1
print(dias_uteis.index("qua"))     # 2

# Convertendo entre lista e tupla
lista = list(dias_uteis)    # tupla → lista (agora mutável)
tupla = tuple(lista)        # lista → tupla

# =============================================================
# SETS (CONJUNTOS) — coleção não-ordenada, sem duplicatas
# =============================================================
# Definidos com chaves {}. Úteis para remover duplicatas
# e fazer operações de conjunto (união, interseção...).

cores = {"vermelho", "azul", "verde", "azul", "vermelho"}
print(cores)  # {'vermelho', 'azul', 'verde'} — sem duplicatas!

# Criando a partir de uma lista com duplicatas
numeros_dup = [1, 2, 2, 3, 3, 3, 4]
sem_dup = set(numeros_dup)
print(sem_dup)  # {1, 2, 3, 4}

# ── Adicionando e removendo ──
cores.add("amarelo")
cores.discard("verde")   # remove sem erro se não existir
print(cores)

# ── Operações de conjunto ──
python_devs = {"Ana", "Bruno", "Carla", "Diego"}
java_devs   = {"Bruno", "Eduardo", "Carla", "Flávia"}

print(python_devs | java_devs)   # União: todos
print(python_devs & java_devs)   # Interseção: em ambos
print(python_devs - java_devs)   # Diferença: só em Python
print(python_devs ^ java_devs)   # Diferença simétrica: em um ou outro, não em ambos

# =============================================================
# RESUMO: QUANDO USAR CADA UM?
# =============================================================
# Lista  → quando a ordem importa e os dados podem mudar
# Tupla  → dados fixos, coordenadas, retorno de funções
# Set    → remover duplicatas, verificar pertencimento, operações de conjunto