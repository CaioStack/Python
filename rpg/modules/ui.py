import time
import sys
import os

# ─── ANSI Colors ─────────────────────────────────────────────────────────────
class Cor:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    DIM     = "\033[2m"

    VERMELHO  = "\033[91m"
    VERDE     = "\033[92m"
    AMARELO   = "\033[93m"
    AZUL      = "\033[94m"
    MAGENTA   = "\033[95m"
    CIANO     = "\033[96m"
    BRANCO    = "\033[97m"
    LARANJA   = "\033[38;5;208m"
    ROXO      = "\033[38;5;141m"
    CINZA     = "\033[38;5;245m"

    BG_VERMELHO = "\033[41m"
    BG_VERDE    = "\033[42m"
    BG_AZUL     = "\033[44m"

def c(texto, cor):
    return f"{cor}{texto}{Cor.RESET}"

def negrito(texto):
    return f"{Cor.BOLD}{texto}{Cor.RESET}"

# ─── Barra de vida visual ─────────────────────────────────────────────────────
def barra_vida(atual, maximo, tamanho=20):
    proporcao = max(0, atual / maximo)
    cheio = int(proporcao * tamanho)
    vazio = tamanho - cheio

    if proporcao > 0.6:
        cor = Cor.VERDE
    elif proporcao > 0.3:
        cor = Cor.AMARELO
    else:
        cor = Cor.VERMELHO

    barra = f"{cor}{'█' * cheio}{Cor.CINZA}{'░' * vazio}{Cor.RESET}"
    return f"[{barra}] {c(str(atual), cor)}/{c(str(maximo), Cor.BRANCO)}"

# ─── Barra de XP ─────────────────────────────────────────────────────────────
def barra_xp(atual, maximo=50, tamanho=15):
    cheio = int((atual / maximo) * tamanho)
    vazio = tamanho - cheio
    barra = f"{Cor.CIANO}{'▓' * cheio}{Cor.CINZA}{'░' * vazio}{Cor.RESET}"
    return f"[{barra}] {c(str(atual), Cor.CIANO)}/{maximo} XP"

# ─── Efeito de digitação ──────────────────────────────────────────────────────
def digitar(texto, delay=0.018):
    for ch in texto:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# ─── Separadores ─────────────────────────────────────────────────────────────
def linha(char="─", tamanho=50, cor=Cor.CINZA):
    print(c(char * tamanho, cor))

def titulo(texto, cor=Cor.CIANO):
    tam = 50
    pad = (tam - len(texto) - 2) // 2
    linha("═", tam, cor)
    print(c("║" + " " * pad + texto + " " * (tam - pad - len(texto) - 2) + "║", cor))
    linha("═", tam, cor)

# ─── Mensagens de ação ───────────────────────────────────────────────────────
def msg_dano(nome, dano, critico=False):
    if critico:
        print(f"  {c('CRÍTICO!', Cor.AMARELO + Cor.BOLD)} {c(nome, Cor.BRANCO)} causou {c(str(dano), Cor.VERMELHO)} de dano!")
    else:
        print(f"  💥 {c(nome, Cor.BRANCO)} causou {c(str(dano), Cor.LARANJA)} de dano!")

def msg_cura(nome, quantidade):
    print(f"  ✨ {c(nome, Cor.BRANCO)} recuperou {c(str(quantidade), Cor.VERDE)} de vida!")

def msg_status(efeito, nome):
    icones = {"veneno": "☠️", "queimadura": "🔥", "paralisia": "⚡"}
    icone = icones.get(efeito, "❓")
    print(f"  {icone} {c(nome, Cor.BRANCO)} sofreu efeito de {c(efeito, Cor.MAGENTA)}!")

def msg_nivel(nome, nivel):
    titulo(f"⬆ {nome} → NÍVEL {nivel}!", Cor.AMARELO)

# ─── Log de batalha (últimas ações) ──────────────────────────────────────────
log_batalha = []

def adicionar_log(texto):
    log_batalha.append(texto)
    if len(log_batalha) > 6:
        log_batalha.pop(0)

def mostrar_log():
    if not log_batalha:
        return
    print(c("\n  📜 Log de batalha:", Cor.CINZA))
    for entrada in log_batalha[-4:]:
        print(c(f"   · {entrada}", Cor.DIM))

def limpar_log():
    log_batalha.clear()

# ─── Pausa dramática ──────────────────────────────────────────────────────────
def pausa(seg=0.8):
    time.sleep(seg)

def limpar_tela():
    os.system('clear' if os.name == 'posix' else 'cls')

# ─── Input com prompt estilizado ─────────────────────────────────────────────
def prompt(texto=""):
    return input(c(f"\n  {texto}>>> ", Cor.CIANO)).strip()

def aguardar():
    input(c("\n  [ENTER para continuar]", Cor.CINZA))
