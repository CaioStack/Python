# Crie um programa que:
# - Leia a quantidade em estoque de 5 produtos
# - Armazene as quantidades em uma lista
# - Mostre quantos produtos estão com estoque menor que 10

estoque = []

for i in range(5):
    quantidade = int(input(f"Digite o estoque do produto {i + 1}: "))
    estoque.append(quantidade)

estoque_baixo = 0
for i in range(len(estoque)):
    if estoque[i] < 10:
        estoque_baixo = estoque_baixo + 1

print(f"Produtos com estoque baixo (menos de 10 unidades): {estoque_baixo}")