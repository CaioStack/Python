# Controle de notas de uma turma

# Crie um programa que:
# - Leia as notas de 10 alunos
# - Armazene as notas em uma lista
# - Calcule a média da turma usando uma função
# - Mostre:
#   - a média da turma
#   - quantos alunos ficaram acima da média
#   - quantos alunos ficaram abaixo da média
#   - a maior nota
#   - a menor nota
# Use apenas: listas, índices, for, while, if/elif/else, funções, variáveis auxiliares

def calcular_media(lista):
    soma = 0
    for i in range(len(lista)):
        soma = soma + lista[i]
    return soma / len(lista)

notas_10 = []

for i in range(10):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    notas_10.append(nota)

media_turma = calcular_media(notas_10)

acima = 0
abaixo = 0
for i in range(len(notas_10)):
    if notas_10[i] > media_turma:
        acima = acima + 1
    elif notas_10[i] < media_turma:
        abaixo = abaixo + 1

maior_nota = notas_10[0]
menor_nota = notas_10[0]
for i in range(1, len(notas_10)):
    if notas_10[i] > maior_nota:
        maior_nota = notas_10[i]
    if notas_10[i] < menor_nota:
        menor_nota = notas_10[i]

print(f"\nMédia da turma: {media_turma:.1f}")
print(f"Alunos acima da média: {acima}")
print(f"Alunos abaixo da média: {abaixo}")
print(f"Maior nota: {maior_nota:.1f}")
print(f"Menor nota: {menor_nota:.1f}")