# Crie um programa que:
# - Leia 8 votos
# - Cada voto pode ser:
#   - 1 para candidato A
#   - 2 para candidato B
#   - 3 para candidato C
# - Armazene os votos em uma lista
# - Mostre quantos votos cada candidato recebeu

votos = []

for i in range(8):
    voto = int(input(f"Voto {i + 1} (1=A, 2=B, 3=C): "))
    votos.append(voto)

votos_a = 0
votos_b = 0
votos_c = 0

for i in range(len(votos)):
    if votos[i] == 1:
        votos_a = votos_a + 1
    elif votos[i] == 2:
        votos_b = votos_b + 1
    elif votos[i] == 3:
        votos_c = votos_c + 1

print(f"Candidato A: {votos_a} voto(s)")
print(f"Candidato B: {votos_b} voto(s)")
print(f"Candidato C: {votos_c} voto(s)")