# Leia uma string digitada pelo usuário e informe:
# - Quantas letras ela possui
# - Quantos números ela possui
# - Quantos outros caracteres ela possui

texto = input("digite uma string: ")

letras = sum(1 for c in texto if c.isalpha())
numeros = sum(1 for c in texto if c.isdigit())
outros = sum(1 for c in texto if not c.isalpha() and not c.isdigit())

print(f"letras: {letras}")
print(f"números: {numeros}")
print(f"outros caracteres: {outros}")