import random
import os
import time
import colorama

try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    COR = True
except ImportError:
    COR = False

def verde(t):   return f"{Fore.GREEN}{t}{Style.RESET_ALL}" if COR else t
def vermelho(t):return f"{Fore.RED}{t}{Style.RESET_ALL}" if COR else t
def amarelo(t): return f"{Fore.YELLOW}{t}{Style.RESET_ALL}" if COR else t
def ciano(t):   return f"{Fore.CYAN}{t}{Style.RESET_ALL}" if COR else t
def negrito(t): return f"{Style.BRIGHT}{t}{Style.RESET_ALL}" if COR else t

NAIPES  = ["♠", "♥", "♦", "♣"]
VALORES = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"Q":10,"K":10,"A":11}
NUM_DECKS = 6

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def carta_arte(valor, naipe):
    v = valor.ljust(2)
    linhas = [
        "┌─────┐",
        f"│{v}   │",
        f"│  {naipe}  │",
        f"│   {v}│",
        "└─────┘",
    ]
    return linhas

def carta_costas():
    return ["┌─────┐","│░░░░░│","│░░░░░│","│░░░░░│","└─────┘"]

def mostrar_cartas(nome, mao, esconder_primeira=False):
    grupos = []
    for i, (v, n) in enumerate(mao):
        if i == 0 and esconder_primeira:
            grupos.append(carta_costas())
        else:
            grupos.append(carta_arte(v, n))

    linhas_unidas = ["  ".join(g[i] for g in grupos) for i in range(5)]
    total_str = "???" if esconder_primeira else str(calcular_total(mao))
    print(f"\n{ciano(nome)} {amarelo(f'[{total_str}]')}")
    for l in linhas_unidas:
        print("  " + l)

def criar_baralho():
    baralho = [(v, n) for _ in range(NUM_DECKS) for n in NAIPES for v in VALORES]
    random.shuffle(baralho)
    return baralho

def calcular_total(mao):
    total = sum(VALORES[c[0]] for c in mao)
    ases = sum(1 for c in mao if c[0] == "A")
    while total > 21 and ases:
        total -= 10
        ases -= 1
    return total

def entrada_aposta(saldo, msg="Quanto deseja apostar? R$"):
    while True:
        try:
            aposta = int(input(amarelo(msg)))
            if 1 <= aposta <= saldo:
                return aposta
            print(vermelho(f"Aposta deve ser entre R$1 e R${saldo}."))
        except ValueError:
            print(vermelho("Digite um número inteiro válido."))

def entrada_opcao(opcoes, prompt):
    while True:
        resp = input(amarelo(prompt)).strip().lower()
        if resp in opcoes:
            return resp
        print(vermelho(f"Opção inválida. Escolha: {', '.join(opcoes)}"))

def turno_jogador(mao, baralho, saldo, aposta, permitir_double=True):
    while True:
        total = calcular_total(mao)
        if total >= 21:
            break

        opcoes = {"c": "comprar", "p": "parar"}
        prompt_parts = ["(c) comprar", "(p) parar"]

        pode_double = permitir_double and len(mao) == 2 and saldo >= aposta
        if pode_double:
            opcoes["d"] = "double"
            prompt_parts.append("(d) double down")

        pode_split = len(mao) == 2 and VALORES[mao[0][0]] == VALORES[mao[1][0]] and saldo >= aposta
        if pode_split:
            opcoes["s"] = "split"
            prompt_parts.append("(s) split")

        escolha = entrada_opcao(opcoes, " | ".join(prompt_parts) + ": ")

        if escolha == "c":
            carta = baralho.pop()
            mao.append(carta)
            print(f"  Você comprou: {verde(carta[0]+carta[1])}")
            mostrar_cartas("Você", mao)

        elif escolha == "p":
            break

        elif escolha == "d":
            carta = baralho.pop()
            mao.append(carta)
            print(f"  Você comprou (double): {verde(carta[0]+carta[1])}")
            mostrar_cartas("Você", mao)
            return aposta * 2  # nova aposta

        elif escolha == "s":
            print(amarelo("\n--- SPLIT ---"))
            mao1 = [mao[0], baralho.pop()]
            mao2 = [mao[1], baralho.pop()]
            ganhos = 0
            for i, m in enumerate([mao1, mao2], 1):
                print(negrito(f"\nMão {i}:"))
                mostrar_cartas(f"Você (mão {i})", m)
                aposta_final = turno_jogador(m, baralho, saldo, aposta, permitir_double=False)
                ganhos += resolver_mao(m, aposta_final)
            return ("split", ganhos)

    return aposta

def turno_dealer(dealer, baralho):
    print(negrito("\n🤖 Turno do dealer..."))
    time.sleep(0.6)
    mostrar_cartas("Dealer", dealer)
    time.sleep(0.6)
    while calcular_total(dealer) < 17:
        carta = baralho.pop()
        dealer.append(carta)
        print(f"  Dealer comprou: {amarelo(carta[0]+carta[1])}")
        mostrar_cartas("Dealer", dealer)
        time.sleep(0.5)

def resolver_mao(mao_jogador, aposta, total_dealer=None):
    total_j = calcular_total(mao_jogador)
    if total_j > 21:
        return -aposta
    if total_dealer is None:
        return 0
    if total_dealer > 21 or total_j > total_dealer:
        return aposta
    elif total_j < total_dealer:
        return -aposta
    return 0

def exibir_resultado(ganho, aposta):
    if ganho > 0:
        print(verde(f"\n🎉 Você ganhou R${ganho}!"))
    elif ganho < 0:
        print(vermelho(f"\n😢 Você perdeu R${abs(ganho)}!"))
    else:
        print(amarelo("\n🤝 Empate!"))

def seguro(dealer, saldo, aposta):
    if dealer[1][0] != "A":
        return 0
    print(amarelo("\nO dealer mostra Ás. Deseja fazer seguro? (s/n): "), end="")
    if input().strip().lower() != "s":
        return 0
    valor_seguro = min(aposta // 2, saldo)
    if calcular_total(dealer) == 21:
        print(verde(f"Dealer tem Blackjack! Seguro pago: R${valor_seguro * 2}"))
        return valor_seguro  # ganho líquido (pagou valor_seguro, recebe valor_seguro*2)
    else:
        print(vermelho(f"Dealer não tem Blackjack. Seguro perdido: R${valor_seguro}"))
        return -valor_seguro

def blackjack():
    limpar()
    print(negrito(ciano("""
  ██████╗ ██╗      █████╗  ██████╗██╗  ██╗     ██╗ █████╗  ██████╗██╗  ██╗
  ██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝     ██║██╔══██╗██╔════╝██║ ██╔╝
  ██████╔╝██║     ███████║██║     █████╔╝      ██║███████║██║     █████╔╝ 
  ██╔══██╗██║     ██╔══██║██║     ██╔═██╗ ██   ██║██╔══██║██║     ██╔═██╗ 
  ██████╔╝███████╗██║  ██║╚██████╗██║  ██╗╚█████╔╝██║  ██║╚██████╗██║  ██╗
  ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
""")))

    saldo = 200
    historico = {"vitorias": 0, "derrotas": 0, "empates": 0}
    rodada = 0

    while saldo > 0:
        rodada += 1
        print(f"\n{'─'*50}")
        print(f"  {negrito('Rodada')} #{rodada}  |  {verde('Saldo: R$' + str(saldo))}  |  "
              f"V:{historico['vitorias']} D:{historico['derrotas']} E:{historico['empates']}")
        print(f"{'─'*50}")

        aposta = entrada_aposta(saldo)
        baralho = criar_baralho()

        jogador = [baralho.pop(), baralho.pop()]
        dealer  = [baralho.pop(), baralho.pop()]

        mostrar_cartas("Você", jogador)
        mostrar_cartas("Dealer", dealer, esconder_primeira=True)

        # Seguro
        ganho_seguro = seguro(dealer, saldo - aposta, aposta)
        saldo += ganho_seguro

        # Blackjack natural
        if calcular_total(jogador) == 21:
            turno_dealer(dealer, baralho)
            if calcular_total(dealer) == 21:
                print(amarelo("\n🤝 Ambos com Blackjack — empate!"))
                historico["empates"] += 1
            else:
                ganho = int(aposta * 1.5)
                print(verde(f"\n🔥 BLACKJACK! Você ganhou R${ganho}!"))
                saldo += ganho
                historico["vitorias"] += 1
        else:
            resultado_turno = turno_jogador(jogador, baralho, saldo, aposta)

            if isinstance(resultado_turno, tuple) and resultado_turno[0] == "split":
                # split já resolveu as mãos contra o dealer internamente
                _, ganho = resultado_turno
                saldo += ganho
                if ganho > 0:   historico["vitorias"] += 1
                elif ganho < 0: historico["derrotas"] += 1
                else:           historico["empates"]  += 1
            else:
                aposta = resultado_turno  # pode ter dobrado

                if calcular_total(jogador) > 21:
                    print(vermelho("\n💥 Você estourou!"))
                    saldo -= aposta
                    historico["derrotas"] += 1
                else:
                    turno_dealer(dealer, baralho)
                    total_dealer = calcular_total(dealer)
                    ganho = resolver_mao(jogador, aposta, total_dealer)
                    exibir_resultado(ganho, aposta)
                    saldo += ganho
                    if ganho > 0:   historico["vitorias"] += 1
                    elif ganho < 0: historico["derrotas"] += 1
                    else:           historico["empates"]  += 1

        print(verde(f"\n💰 Saldo atual: R${saldo}"))

        if saldo <= 0:
            print(vermelho("\n💸 Você ficou sem saldo!"))
            break

        if entrada_opcao({"s","n"}, "\nJogar novamente? (s/n): ") == "n":
            break

    print(negrito(f"""
{'─'*50}
  🏁 Fim de jogo!
  Rodadas jogadas : {rodada}
  Vitórias        : {historico['vitorias']}
  Derrotas        : {historico['derrotas']}
  Empates         : {historico['empates']}
  Saldo final     : R${saldo}
{'─'*50}"""))

if __name__ == "__main__":
    blackjack()
