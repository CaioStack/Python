# Crie uma função chamada jogo_adivinhacao que gera aleatoriamente
# um número inteiro entre 1 e 100 e permite que o jogador tente
# adivinhar o número. A função deve dar dicas se o palpite do
# jogador estiver muito alto ou muito baixo. Conte o número de
# tentativas e, no final, informe quantas tentativas foram
# necessárias para acertar o número.

from random import randint

def jogo_adivinhacao():
    numero_secreto = randint(1, 100)
    tentativas = 0
 
    print("Adivinhe o número entre 1 e 100!")
 
    while True:
        palpite = int(input("Seu palpite: "))
        tentativas = tentativas + 1
 
        if palpite < numero_secreto:
            print("Muito baixo! Tente um número maior.")
        elif palpite > numero_secreto:
            print("Muito alto! Tente um número menor.")
        else:
            print(f"Parabéns! Você acertou o número {numero_secreto}!")
            print(f"Total de tentativas: {tentativas}")
            break

jogo_adivinhacao()