# =============================================================
# EXERCÍCIOS
# =============================================================

# Exercício 1:
# Crie uma lista com 5 números inteiros. Sem usar sort(),
# encontre o maior e o menor valor. (Dica: use max() e min())

numeros = [12, 7, 25, 3, 18]

maior = max(numeros)
menor = min(numeros)

print("Maior valor:", maior)
print("Menor valor:", menor)

# Exercício 2:
# Dada a lista [1, 2, 2, 3, 4, 4, 4, 5], remova todos os
# duplicados e exiba os elementos únicos em ordem crescente.

lista = [1, 2, 2, 3, 4, 4, 4, 5]

unicos = sorted(set(lista))

print("Elementos únicos:", unicos)

# Exercício 3:
# Crie duas listas de alunos de duas turmas. Use sets para
# descobrir quais alunos estão nas duas turmas.

turma1 = {"Ana", "Carlos", "João", "Maria"}
turma2 = {"Pedro", "Maria", "João", "Lucas"}

alunos_em_ambas = turma1.intersection(turma2)

print("Alunos nas duas turmas:", alunos_em_ambas)

# Exercício 4:
# Crie uma lista com os nomes de 5 pessoas. Ordene-a por
# tamanho do nome (do menor para o maior).

nomes = ["Caio", "Fernanda", "Ana", "Ricardo", "Lu"]

nomes.sort(key=len)

print("Nomes ordenados por tamanho:")
print(nomes)