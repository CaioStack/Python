import random
import time
import json
import os
import unicodedata

# ─── Cores ANSI ────────────────────────────────────────────────────────────────
class Cor:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    VERMELHO = "\033[91m"
    VERDE    = "\033[92m"
    AMARELO  = "\033[93m"
    AZUL     = "\033[94m"
    MAGENTA  = "\033[95m"
    CIANO    = "\033[96m"
    BRANCO   = "\033[97m"
    CINZA    = "\033[90m"

def colorir(texto, cor):
    return f"{cor}{texto}{Cor.RESET}"

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

# ─── Arquivos de dados ─────────────────────────────────────────────────────────
ARQUIVO_PALAVRAS   = "palavras.json"
ARQUIVO_RECORDES   = "recordes.json"

def carregar_palavras():
    if not os.path.exists(ARQUIVO_PALAVRAS):
        print(colorir(
            f"⚠️  Arquivo '{ARQUIVO_PALAVRAS}' não encontrado.\n"
            "   Coloque-o na mesma pasta que este script.", Cor.VERMELHO))
        raise SystemExit(1)
    with open(ARQUIVO_PALAVRAS, "r", encoding="utf-8") as f:
        return json.load(f)

def carregar_recordes():
    if os.path.exists(ARQUIVO_RECORDES):
        with open(ARQUIVO_RECORDES, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_recordes(recordes):
    with open(ARQUIVO_RECORDES, "w", encoding="utf-8") as f:
        json.dump(recordes, f, ensure_ascii=False, indent=2)

# ─── Normalização (ignora acentos na comparação) ───────────────────────────────
def normalizar(texto):
    return unicodedata.normalize("NFD", texto).encode("ascii", "ignore").decode("ascii").lower()

# ─── Estágios da forca ─────────────────────────────────────────────────────────
ESTAGIOS = [
    r"""
   ┌─────┐
   │     │
   │
   │
   │
   │
═══╧═══════
""",
    r"""
   ┌─────┐
   │     │
   │     O
   │
   │
   │
═══╧═══════
""",
    r"""
   ┌─────┐
   │     │
   │     O
   │     │
   │
   │
═══╧═══════
""",
    r"""
   ┌─────┐
   │     │
   │     O
   │    /│
   │
   │
═══╧═══════
""",
    r"""
   ┌─────┐
   │     │
   │     O
   │    /│\
   │
   │
═══╧═══════
""",
    r"""
   ┌─────┐
   │     │
   │     O
   │    /│\
   │    /
   │
═══╧═══════
""",
    r"""
   ┌─────┐
   │     │
   │     O
   │    /│\
   │    / \
   │
═══╧═══════
""",
]

ANIMACAO_VITORIA = r"""
    \o/
     |
    / \
  🎉 VENCEU! 🎉
"""

ANIMACAO_DERROTA = r"""
   ┌─────┐
   │     │
   │     O
   │    /│\
   │    / \
   │
═══╧═══════
  💀 Game Over
"""

# ─── Cálculo de pontuação ──────────────────────────────────────────────────────
BONUS_DIFICULDADE = {"facil": 100, "medio": 200, "dificil": 350}
PENALIDADE_ERRO   = 30
PENALIDADE_DICA   = 50
BONUS_TEMPO       = 5   # pontos por segundo sobrando (se houver tempo limite)

def calcular_pontuacao(dificuldade, erros, dica_usada, tempo_limite, tempo_gasto, venceu):
    if not venceu:
        return 0
    base  = BONUS_DIFICULDADE[dificuldade]
    base -= erros * PENALIDADE_ERRO
    if dica_usada:
        base -= PENALIDADE_DICA
    if tempo_limite:
        sobrou = max(0, tempo_limite - tempo_gasto)
        base  += int(sobrou * BONUS_TEMPO)
    return max(base, 10)   # mínimo 10 pontos por vencer

# ─── Recordes ─────────────────────────────────────────────────────────────────
def mostrar_recordes(recordes):
    limpar()
    print(colorir("🏆  TOP 10 RECORDES", Cor.AMARELO + Cor.BOLD))
    print(colorir("─" * 45, Cor.CINZA))
    if not recordes:
        print(colorir("  Nenhum recorde ainda. Seja o primeiro!", Cor.CINZA))
    else:
        for i, r in enumerate(recordes[:10], 1):
            medalha = ["🥇","🥈","🥉"].get(i - 1, f" {i}.")
            linha = (f"  {medalha}  {r['nome']:<15}"
                     f"{colorir(str(r['pontos']) + ' pts', Cor.CIANO)}"
                     f"  {r['tema']}/{r['dificuldade']}")
            print(linha)
    print(colorir("─" * 45, Cor.CINZA))
    input(colorir("\nPressione Enter para voltar...", Cor.CINZA))

def registrar_recorde(recordes, nome, pontos, tema, dificuldade):
    recordes.append({"nome": nome, "pontos": pontos,
                     "tema": tema, "dificuldade": dificuldade})
    recordes.sort(key=lambda r: r["pontos"], reverse=True)
    salvar_recordes(recordes)

# ─── Menus de seleção ──────────────────────────────────────────────────────────
def menu_opcoes(titulo, opcoes, cor=Cor.CIANO):
    print(colorir(titulo, Cor.BOLD))
    for op in opcoes:
        print(colorir(f"  • {op}", cor))
    while True:
        escolha = input(colorir("  ▶ ", Cor.AMARELO)).strip().lower()
        if escolha in [normalizar(o) for o in opcoes]:
            return escolha
        if escolha in opcoes:
            return escolha
        print(colorir("  ⚠️  Opção inválida. Tente novamente.", Cor.VERMELHO))

def escolher_tema(temas):
    return menu_opcoes("📚 Escolha um tema:", list(temas.keys()))

def escolher_dificuldade():
    return menu_opcoes("🎯 Escolha a dificuldade:", ["facil", "medio", "dificil"])

def escolher_tempo():
    resposta = input(colorir("\n⏱️  Deseja tempo limite por jogada? (s/n): ", Cor.AZUL)).strip().lower()
    if resposta == "s":
        while True:
            try:
                segundos = int(input(colorir("   Quantos segundos? ", Cor.AZUL)))
                if segundos > 0:
                    return segundos
            except ValueError:
                pass
            print(colorir("   ⚠️  Valor inválido.", Cor.VERMELHO))
    return None

# ─── Exibição da forca colorida ────────────────────────────────────────────────
def exibir_forca(erros):
    cor = Cor.VERDE if erros == 0 else (Cor.AMARELO if erros < 4 else Cor.VERMELHO)
    print(colorir(ESTAGIOS[erros], cor))

# ─── Exibir palavra com cores ──────────────────────────────────────────────────
def exibir_palavra(descobertas, palavra_original):
    resultado = []
    for ch in descobertas:
        if ch == "_":
            resultado.append(colorir("_", Cor.CINZA))
        else:
            resultado.append(colorir(ch, Cor.VERDE + Cor.BOLD))
    print("  " + " ".join(resultado))

def exibir_letras_usadas(usadas, palavra_norm):
    certas  = [colorir(l, Cor.VERDE)   for l in sorted(usadas) if l in palavra_norm]
    erradas = [colorir(l, Cor.VERMELHO) for l in sorted(usadas) if l not in palavra_norm]
    todas   = certas + erradas
    print(colorir("  Letras usadas: ", Cor.CINZA) + " ".join(todas) if todas else "")

# ─── Streak ───────────────────────────────────────────────────────────────────
def exibir_streak(streak):
    if streak >= 2:
        chamas = "🔥" * min(streak, 5)
        print(colorir(f"  {chamas} Sequência de vitórias: {streak}!", Cor.AMARELO))

# ─── Classe principal do jogo ──────────────────────────────────────────────────
class JogoDaForca:
    MAX_ERROS = 6

    def __init__(self, entrada, dificuldade, tempo_limite):
        self.palavra_original = entrada["palavra"]
        self.dica_texto       = entrada["dica"]
        self.dificuldade      = dificuldade
        self.tempo_limite     = tempo_limite

        self.palavra_norm     = normalizar(self.palavra_original)
        self.descobertas      = ["_"] * len(self.palavra_norm)
        self.letras_usadas    = []
        self.erros            = 0
        self.dica_usada       = False
        self.tempo_total_gasto = 0.0

    def _pedir_dica(self):
        self.dica_usada = True
        print(colorir(f"\n  💡 Dica: {self.dica_texto}", Cor.MAGENTA))
        print(colorir(f"     (−{PENALIDADE_DICA} pontos)", Cor.CINZA))

    def _processar_letra(self, chute):
        chute_norm = normalizar(chute)
        if len(chute_norm) != 1 or not chute_norm.isalpha():
            print(colorir("  ⚠️  Digite apenas uma letra válida!", Cor.AMARELO))
            return
        if chute_norm in self.letras_usadas:
            print(colorir("  ⚠️  Você já tentou essa letra!", Cor.AMARELO))
            return

        self.letras_usadas.append(chute_norm)

        if chute_norm in self.palavra_norm:
            print(colorir("  ✅  Acertou!", Cor.VERDE))
            for i, ch in enumerate(self.palavra_norm):
                if ch == chute_norm:
                    self.descobertas[i] = self.palavra_original[i]
        else:
            self.erros += 1
            restam = self.MAX_ERROS - self.erros
            print(colorir(f"  ❌  Errou! Restam {restam} erro(s).", Cor.VERMELHO))

    def _tentar_palavra(self):
        tentativa = input(colorir("  ✍️  Digite a palavra inteira: ", Cor.CIANO)).strip().lower()
        if normalizar(tentativa) == self.palavra_norm:
            # Revela tudo
            self.descobertas = list(self.palavra_original)
            print(colorir("  🎯  Palavra correta!", Cor.VERDE))
        else:
            self.erros += 1
            print(colorir(f"  ❌  Palavra errada! Você perde uma vida.", Cor.VERMELHO))

    def jogar(self):
        while self.erros < self.MAX_ERROS and "_" in self.descobertas:
            limpar()
            exibir_forca(self.erros)

            print(colorir(f"  Tema: {colorir(tema_atual, Cor.CIANO)} │ "
                          f"Dificuldade: {colorir(self.dificuldade, Cor.MAGENTA)} │ "
                          f"Erros: {colorir(str(self.erros), Cor.VERMELHO)}/{self.MAX_ERROS}",
                          Cor.CINZA))
            print()
            exibir_palavra(self.descobertas, self.palavra_original)
            print()
            exibir_letras_usadas(self.letras_usadas, self.palavra_norm)
            print()

            if self.tempo_limite:
                print(colorir(f"  ⏱️  Você tem {self.tempo_limite}s para responder.", Cor.AZUL))

            print(colorir("\n  [letra]  Chute uma letra", Cor.BRANCO))
            if not self.dica_usada:
                print(colorir("  [!]      Pedir dica (−50 pts)", Cor.CINZA))
            print(colorir("  [*]      Tentar a palavra inteira", Cor.CINZA))
            print()

            inicio = time.time()
            entrada_bruta = input(colorir("  ▶ ", Cor.AMARELO)).strip()
            fim = time.time()
            tempo_jogada = fim - inicio
            self.tempo_total_gasto += tempo_jogada

            if self.tempo_limite and tempo_jogada > self.tempo_limite:
                print(colorir("\n  ⏰  Tempo esgotado! +1 erro.", Cor.VERMELHO))
                self.erros += 1
                time.sleep(1.2)
                continue

            if entrada_bruta == "!":
                if not self.dica_usada:
                    self._pedir_dica()
                else:
                    print(colorir("  ⚠️  Dica já utilizada.", Cor.CINZA))
                time.sleep(1.5)
                continue

            if entrada_bruta == "*":
                self._tentar_palavra()
                time.sleep(1.2)
                continue

            self._processar_letra(entrada_bruta)
            time.sleep(0.9)

        venceu = "_" not in self.descobertas
        return venceu, self.erros, self.dica_usada, self.tempo_total_gasto

# ─── Tela de resultado ─────────────────────────────────────────────────────────
def tela_resultado(venceu, erros, pontos, streak, palavra_original):
    limpar()
    if venceu:
        print(colorir(ANIMACAO_VITORIA, Cor.VERDE + Cor.BOLD))
        print(colorir(f"  Palavra: {palavra_original.upper()}", Cor.BRANCO + Cor.BOLD))
        print(colorir(f"  Pontuação: {pontos} pts", Cor.AMARELO + Cor.BOLD))
        if streak >= 2:
            print(colorir(f"  🔥 Sequência de {streak} vitórias!", Cor.AMARELO))
    else:
        print(colorir(ANIMACAO_DERROTA, Cor.VERMELHO))
        print(colorir(f"  A palavra era: {palavra_original.upper()}", Cor.BRANCO + Cor.BOLD))
        print(colorir("  Sem pontos desta vez.", Cor.CINZA))
    print()

# ─── Menu principal ────────────────────────────────────────────────────────────
def menu_principal():
    limpar()
    banner = r"""
  ╔═══════════════════════════════════════╗
  ║       🪢  JOGO DA FORCA  🪢           ║
  ║       versão avançada                 ║
  ╚═══════════════════════════════════════╝
"""
    print(colorir(banner, Cor.CIANO + Cor.BOLD))
    print(colorir("  [1]  Jogar", Cor.BRANCO))
    print(colorir("  [2]  Ver recordes", Cor.BRANCO))
    print(colorir("  [3]  Sair\n", Cor.BRANCO))
    return input(colorir("  ▶ ", Cor.AMARELO)).strip()

# ─── Loop principal ────────────────────────────────────────────────────────────
def main():
    temas      = carregar_palavras()
    recordes   = carregar_recordes()
    streak     = 0
    pontos_sessao = 0

    global tema_atual  # usado dentro de JogoDaForca para exibir

    while True:
        try:
            opcao = menu_principal()
        except KeyboardInterrupt:
            print(colorir("\n\n  👋  Até logo!\n", Cor.CIANO))
            break

        if opcao == "3":
            print(colorir("\n  👋  Valeu por jogar!\n", Cor.CIANO))
            break

        if opcao == "2":
            mostrar_recordes(recordes)
            continue

        if opcao != "1":
            continue

        # ── Configuração da partida ────────────────────────────────────────────
        limpar()
        print(colorir("  ─── Nova Partida ───\n", Cor.BOLD))
        exibir_streak(streak)

        tema_atual   = escolher_tema(temas)
        dificuldade  = escolher_dificuldade()
        tempo_limite = escolher_tempo()

        entrada = random.choice(temas[tema_atual][dificuldade])

        # ── Jogar ─────────────────────────────────────────────────────────────
        jogo = JogoDaForca(entrada, dificuldade, tempo_limite)
        try:
            venceu, erros, dica_usada, tempo_gasto = jogo.jogar()
        except KeyboardInterrupt:
            print(colorir("\n\n  ⏹  Partida encerrada.\n", Cor.AMARELO))
            streak = 0
            continue

        # ── Pontuação e streak ────────────────────────────────────────────────
        pontos = calcular_pontuacao(dificuldade, erros, dica_usada,
                                    tempo_limite, tempo_gasto, venceu)
        if venceu:
            streak        += 1
            pontos_sessao += pontos
            # Bônus de streak
            if streak >= 3:
                bonus_streak = 50 * (streak - 2)
                pontos       += bonus_streak
                pontos_sessao += bonus_streak
        else:
            streak = 0

        tela_resultado(venceu, erros, pontos, streak, entrada["palavra"])

        # ── Recorde ───────────────────────────────────────────────────────────
        if venceu and pontos > 0:
            if recordes and pontos > recordes[0]["pontos"]:
                print(colorir("  🏆  NOVO RECORDE GERAL!", Cor.AMARELO + Cor.BOLD))
            nome = input(colorir("  Seu nome para o placar (Enter para pular): ",
                                 Cor.CIANO)).strip()
            if nome:
                registrar_recorde(recordes, nome, pontos, tema_atual, dificuldade)
                print(colorir("  ✅  Pontuação registrada!", Cor.VERDE))

        print(colorir(f"\n  Pontos nesta sessão: {pontos_sessao}", Cor.AMARELO))
        print()

        try:
            continuar = input(colorir("  Jogar novamente? (s/n): ", Cor.CIANO)).strip().lower()
        except KeyboardInterrupt:
            continuar = "n"

        if continuar != "s":
            print(colorir(f"\n  👋  Fim de sessão! Total de pontos: {pontos_sessao}\n",
                          Cor.CIANO + Cor.BOLD))
            break

if __name__ == "__main__":
    main()
