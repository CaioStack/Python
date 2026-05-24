# Crie uma função chamada eh_par que recebe um número como
# argumento e imprime na tela "Verdade, é par" se o número
# for par e "Falso, é ímpar" se for ímpar.
# Peça ao usuário para inserir um número e informe se é par
# ou ímpar através da função criada.

def eh_par(numero):
    if numero % 2 == 0:
        print("Verdade, é par")
    else:
        print("Falso, é ímpar")

num_par = int(input("Digite um número: "))
eh_par(num_par)