# Crie uma função chamada fatorial que calcula e retorna o
# fatorial de um número inteiro não negativo. Seu programa
# deve solicitar um número ao usuário e chamar a função fatorial
# para mostrar o fatorial do número lido.

def fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    resultado = 1
    i = 2
    while i <= numero:
        resultado = resultado * i
        i = i + 1
    return resultado

num_fat = int(input("Digite um número inteiro não negativo: "))
print(f"Fatorial de {num_fat} = {fatorial(num_fat)}")