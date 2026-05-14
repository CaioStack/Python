# Leia uma palavra digitada pelo usuário e mostre uma nova palavra em que o primeiro caractere seja substituído por 0.

palavra = input("digite uma palavra: ")

nova_palavra = "0" + palavra[1:]

print(nova_palavra)