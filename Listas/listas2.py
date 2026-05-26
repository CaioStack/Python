# Crie um programa que:
# - Leia as notas de 6 alunos
# - Armazene as notas em uma lista
# - Conte quantos alunos tiveram nota maior ou igual a 7

notas_turma = []

for i in range(6):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    notas_turma.append(nota)

aprovados = 0
for i in range(len(notas_turma)):
    if notas_turma[i] >= 7:
        aprovados = aprovados + 1

print(f"Quantidade de alunos aprovados: {aprovados}")