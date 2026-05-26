# Crie um programa que:
# - Leia 4 notas de um aluno
# - Armazene as notas em uma lista
# - Calcule a média
# - Mostre se o aluno ficou aprovado ou reprovado
# Critério:
# - Média maior ou igual a 6: aprovado
# - Média menor que 6: reprovado

notas = []

for i in range(4):
    nota = float(input(f"Digite a nota {i + 1}: "))
    notas.append(nota)

soma = 0
for i in range(len(notas)):
    soma = soma + notas[i]

media = soma / len(notas)

print(f"Média: {media:.1f}")

if media >= 6:
    print("Resultado: Aprovado")
else:
    print("Resultado: Reprovado")