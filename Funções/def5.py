# Crie uma função chamada eh_primo que recebe um número como
# argumento e retorna True se ele for primo e False se não for.
# Peça ao usuário para inserir um número, verifique e informe
# ao usuário se ele é primo ou não. Seu programa deve informar
# "Primo" ou "Não é primo".

def eh_primo(numero):
    if numero < 2:
        return False
    i = 2
    while i < numero:
        if numero % i == 0:
            return False
        i = i + 1
    return True

num_primo = int(input("Digite um número: "))

if eh_primo(num_primo):
    print("Primo")
else:
    print("Não é primo")