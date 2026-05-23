# Crie um programa que:
# - Leia 7 temperaturas
# - Armazene as temperaturas em uma lista
# - Calcule a média da semana
# - Mostre quantos dias tiveram temperatura acima da média

temperaturas = []

for i in range(7):
    temp = float(input(f"Digite a temperatura do dia {i + 1}: "))
    temperaturas.append(temp)

soma_temp = 0
for i in range(len(temperaturas)):
    soma_temp = soma_temp + temperaturas[i]

media_temp = soma_temp / len(temperaturas)

dias_acima = 0
for i in range(len(temperaturas)):
    if temperaturas[i] > media_temp:
        dias_acima = dias_acima + 1

print(f"Média da semana: {media_temp:.1f}°C")
print(f"Dias acima da média: {dias_acima}")