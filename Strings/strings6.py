# Leia uma frase digitada pelo usuário e conte quantas vogais ela possui. O programa deve funcionar mesmo se o usuário digitar letras maiúsculas.

frase = input("digite uma frase: ")
vogais = "aeiou"
total = sum(1 for letra in frase.lower() if letra in vogais)
print(f"Total de vogais: {total}")