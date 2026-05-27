# =============================================================
# EXERCÍCIOS
# =============================================================

# Exercício 1:
# Calcule a área de um retângulo com base 7.5 e altura 4.2.
# Exiba o resultado formatado com 2 casas decimais.
# Dica: f"{valor:.2f}"

base = 7.5
altura = 4.2

area = base * altura

print(f"A área do retângulo é {area:.2f}")

# Exercício 2:
# Um produto custa R$150,00. Calcule:
# a) O valor com 15% de desconto
# b) O valor parcelado em 3x (sem juros)
# c) Se o produto está abaixo de R$200 (True/False)

produto = 150.00

# a) 15% de desconto
desconto = produto * 0.15
valor_desconto = produto - desconto

# b) Parcelado em 3x
parcela = produto / 3

# c) Verificar se está abaixo de R$200
abaixo_200 = produto < 200

print(f"Valor com desconto: R${valor_desconto:.2f}")
print(f"3x de R${parcela:.2f}")
print(f"O produto está abaixo de R$200? {abaixo_200}")

# Exercício 3:
# Dado um número inteiro, verifique se ele é par (use %).
# Um número é par quando n % 2 == 0.

numero = int(input("Digite um número inteiro: "))

par = numero % 2 == 0

print(f"O número {numero} é par? {par}")