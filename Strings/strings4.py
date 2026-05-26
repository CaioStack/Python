# Leia uma palavra digitada pelo usuário e mostre uma nova palavra em que o último caractere seja substituído por #.

palavra = input("digite uma palavra: ")

nova_palavra = palavra[:-1] + "#"

print(nova_palavra)