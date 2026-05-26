import random
import time

from modules.ui import (c, Cor, negrito, barra_vida, linha, titulo,
                         mostrar_log, limpar_log, pausa, aguardar, prompt, digitar)
from modules.itens import usar_item, equipar_item, abrir_loja
from modules.personagens import criar_inimigo

# ─── Status de batalha ────────────────────────────────────────────────────────
def mostrar_hud(jogador, inimigo):
    print()
    linha("─", 52, Cor.CINZA)

    # Jogador
    icone_classe = {"Guerreiro": "⚔️", "Mago": "🧙", "Arqueiro": "🏹"}.get(jogador.classe, "🧑")
    nivel_str = c(f"Nv.{jogador.nivel}", Cor.AMARELO)
    print(f"  {icone_classe} {c(jogador.nome, Cor.BRANCO)} {nivel_str}")
    print(f"     HP  {barra_vida(jogador.vida, jogador.vida_max)}")

    # Status do jogador
    if jogador.status_efeitos:
        status_str = "  ".join([f"{c(k, Cor.MAGENTA)}({v}t)" for k, v in jogador.status_efeitos.items()])
        print(f"     ⚠️  {status_str}")

    linha("·" * 52, 1, Cor.CINZA)

    # Inimigo
    chefe_tag = c(" [CHEFE]", Cor.VERMELHO + Cor.BOLD) if inimigo.chefe else ""
    fase_tag = c(f" [Fase {inimigo.fase}]", Cor.LARANJA) if inimigo.chefe and inimigo.fase > 1 else ""
    print(f"  {inimigo.icone} {c(inimigo.nome, Cor.VERMELHO)}{chefe_tag}{fase_tag}")
    print(f"     HP  {barra_vida(inimigo.vida, inimigo.vida_max)}")

    if inimigo.status_efeitos:
        status_str = "  ".join([f"{c(k, Cor.MAGENTA)}({v}t)" for k, v in inimigo.status_efeitos.items()])
        print(f"     ⚠️  {status_str}")

    linha("─", 52, Cor.CINZA)
    mostrar_log()

# ─── Menu de habilidades ──────────────────────────────────────────────────────
def menu_habilidades(jogador, inimigo):
    from modules.personagens import HABILIDADES
    hab = jogador.habilidades_disponiveis
    if not hab:
        print(c("  Nenhuma habilidade disponível ainda.", Cor.CINZA))
        return False

    print(c("\n  🔮 Habilidades:", Cor.CIANO))
    for i, chave in enumerate(hab):
        h = HABILIDADES[chave]
        cd = jogador.cooldowns.get(chave, 0)
        cd_str = c(f"  ⏳ {cd}t", Cor.AMARELO) if cd > 0 else c("  ✅ pronto", Cor.VERDE)
        print(f"  {c(str(i+1), Cor.AMARELO)}. {h['icone']} {c(h['nome'], Cor.BRANCO)} — {c(h['desc'], Cor.CINZA)}{cd_str}")
    print(f"  {c('0', Cor.CINZA)}. Voltar")

    try:
        escolha = int(input(c("  >>> ", Cor.CIANO)))
    except ValueError:
        return False

    if escolha == 0:
        return False

    return jogador.usar_habilidade(inimigo, escolha - 1)

# ─── Turno do jogador ─────────────────────────────────────────────────────────
def turno_jogador(jogador, inimigo):
    # Paralisia impede ação
    if "paralisia" in jogador.status_efeitos:
        print(f"\n  ⚡ {c(jogador.nome + ' está paralisado!', Cor.AMARELO)} Turno perdido!")
        pausa(1)
        return

    while True:
        print(c("\n  ⚔️  SEU TURNO", Cor.VERDE + Cor.BOLD))
        print(f"  {c('1', Cor.AMARELO)}. Atacar")
        print(f"  {c('2', Cor.AMARELO)}. Defender")
        print(f"  {c('3', Cor.AMARELO)}. Habilidade")
        print(f"  {c('4', Cor.AMARELO)}. Usar item  {c(f'({jogador.inventario.num_consumiveis()} consumíveis)', Cor.CINZA)}")
        print(f"  {c('5', Cor.AMARELO)}. Equipar item")
        print(f"  {c('6', Cor.AMARELO)}. Ver status")

        escolha = input(c("  >>> ", Cor.CIANO)).strip()

        if escolha == "1":
            jogador.atacar(inimigo)
            break
        elif escolha == "2":
            jogador.defender()
            break
        elif escolha == "3":
            if menu_habilidades(jogador, inimigo):
                break
        elif escolha == "4":
            if usar_item(jogador, jogador.inventario, inimigo):
                break
        elif escolha == "5":
            equipar_item(jogador, jogador.inventario)
            # Não consome turno, mas mostra menu novamente
        elif escolha == "6":
            jogador.mostrar_status_completo()
        else:
            print(c("  ⚠️  Opção inválida!", Cor.VERMELHO))

# ─── Turno do inimigo ────────────────────────────────────────────────────────
def turno_inimigo(jogador, inimigo):
    print(c(f"\n  👹 Turno de {inimigo.nome}...", Cor.VERMELHO))
    pausa(0.7)
    inimigo.escolher_acao(jogador)

# ─── Batalha principal ────────────────────────────────────────────────────────
def batalha(jogador, vitorias):
    limpar_log()
    chefe = (vitorias > 0 and vitorias % 5 == 0)
    inimigo = criar_inimigo(vitorias, forca_chefe=chefe)

    if inimigo.chefe:
        titulo(f"👿 CHEFE: {inimigo.nome} {inimigo.icone}", Cor.VERMELHO)
        digitar(f"  Um {inimigo.nome} lendário bloqueia seu caminho!", delay=0.03)
    else:
        print(f"\n  ⚠️  {c('Um ' + inimigo.icone + ' ' + inimigo.nome + ' apareceu!', Cor.LARANJA)}")

    pausa(0.8)
    turno = 1

    while jogador.esta_vivo() and inimigo.esta_vivo():
        mostrar_hud(jogador, inimigo)
        print(c(f"\n  — Turno {turno} —", Cor.CINZA))

        # Turno do jogador
        turno_jogador(jogador, inimigo)

        # Processar status do inimigo
        if inimigo.esta_vivo():
            inimigo.processar_status()

        if not inimigo.esta_vivo():
            break

        # Turno do inimigo
        turno_inimigo(jogador, inimigo)

        # Processar status do jogador
        if jogador.esta_vivo():
            jogador.processar_status()

        # Reduzir cooldowns
        jogador.reduzir_cooldowns()
        inimigo.reduzir_cooldowns()

        turno += 1
        pausa(0.3)

    # ── Resultado ──────────────────────────────────────────────────────────
    mostrar_hud(jogador, inimigo)

    if jogador.esta_vivo():
        print(f"\n  {c('🏆 VITÓRIA!', Cor.VERDE + Cor.BOLD)} Você derrotou {inimigo.icone} {c(inimigo.nome, Cor.BRANCO)}!")
        ouro_ganho = inimigo.droppar_ouro()
        if inimigo.chefe:
            ouro_ganho = int(ouro_ganho * 1.5)
        jogador.ouro += ouro_ganho
        print(f"  💰 +{c(str(ouro_ganho), Cor.AMARELO)} ouro!")
        jogador.ganhar_xp(inimigo.xp_recompensa)
        return True
    else:
        print(f"\n  {c('💀 DERROTA!', Cor.VERMELHO + Cor.BOLD)} Você foi derrotado...")
        return False

# ─── Entre batalhas: loja e cura ─────────────────────────────────────────────
def entre_batalhas(jogador, vitorias):
    print()
    linha("═", 52, Cor.CIANO)
    # Cura parcial
    cura = int(jogador.vida_max * 0.25)
    jogador.vida = min(jogador.vida + cura, jogador.vida_max)
    print(f"  ✨ Descansou e recuperou {c(str(cura), Cor.VERDE)} HP!")

    print(f"\n  {c('O', Cor.AMARELO)}. Abrir loja do aventureiro")
    print(f"  {c('C', Cor.VERDE)}. Continuar para próxima batalha")
    print(f"  {c('S', Cor.VERMELHO)}. Salvar e sair")

    while True:
        escolha = input(c("\n  >>> ", Cor.CIANO)).strip().lower()
        if escolha == "o":
            abrir_loja(jogador)
        elif escolha == "c":
            return True
        elif escolha == "s":
            return False
        else:
            print(c("  ⚠️  Opção inválida!", Cor.VERMELHO))
