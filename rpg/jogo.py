#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════╗
║           ⚔️  RPG TERMINAL  —   by.Caio  ⚔️         ║
║                                                      ║
╚══════════════════════════════════════════════════════╝
"""

import sys
import os

# Adiciona o diretório do script ao path
sys.path.insert(0, os.path.dirname(__file__))

from modules.ui import (c, Cor, titulo, linha, digitar,
                         pausa, aguardar, limpar_tela)
from modules.personagens import escolher_classe
from modules.batalha import batalha, entre_batalhas
from modules.saves import (salvar_jogo, carregar_jogo, listar_saves,
                            salvar_recorde, mostrar_recordes)


# ─── Tela de título ──────────────────────────────────────────────────────────
def tela_titulo():
    limpar_tela()
    print(c("""
  ╔══════════════════════════════════════════════════╗
  ║                                                  ║
  ║      ⚔️   R P G   T E R M I N A L   ⚔️          ║
  ║                   by.Caio                        ║
  ║                  Versão 1.0                      ║
  ║                                                  ║
  ╚══════════════════════════════════════════════════╝
""", Cor.CIANO + Cor.BOLD))

    print(f"  {c('1', Cor.AMARELO)}. Novo Jogo")
    print(f"  {c('2', Cor.AMARELO)}. Carregar Jogo")
    print(f"  {c('3', Cor.AMARELO)}. Hall da Fama 🏆")
    print(f"  {c('4', Cor.AMARELO)}. Sair")
    linha()

    while True:
        escolha = input(c("  >>> ", Cor.CIANO)).strip()
        if escolha in ("1", "2", "3", "4"):
            return escolha
        print(c("  ⚠️  Opção inválida!", Cor.VERMELHO))


# ─── Menu de saves ────────────────────────────────────────────────────────────
def menu_saves(acao="salvar"):
    titulo(f"{'💾 SALVAR' if acao == 'salvar' else '📂 CARREGAR'} JOGO", Cor.AZUL)
    saves = listar_saves()

    for slot, dados in saves:
        if dados:
            print(f"  {c(str(slot), Cor.AMARELO)}. {c(dados['nome'], Cor.BRANCO)} ({dados['classe']}) "
                  f"— Nv.{dados['nivel']}  {dados['vitorias']} vitórias  {c(dados['data'], Cor.CINZA)}")
        else:
            print(f"  {c(str(slot), Cor.AMARELO)}. {c('(vazio)', Cor.CINZA)}")

    print(f"  {c('0', Cor.CINZA)}. Cancelar")
    linha()

    try:
        slot = int(input(c("  Slot: ", Cor.CIANO)))
        if slot == 0:
            return None
        return slot
    except ValueError:
        return None


# ─── Fluxo principal ─────────────────────────────────────────────────────────
def novo_jogo():
    limpar_tela()
    titulo("⚔️  NOVA AVENTURA", Cor.VERDE)
    digitar("\n  Bem-vindo, aventureiro! Sua jornada começa agora.", delay=0.02)
    pausa(0.5)

    jogador = escolher_classe()
    print(f"\n  ✅ {c(jogador.classe, Cor.CIANO)} selecionado! Boa sorte, {c(jogador.nome, Cor.BRANCO)}!")
    aguardar()
    return jogador, 0


def jogo_principal(jogador, vitorias):
    while True:
        limpar_tela()

        # Aviso de chefe
        if vitorias > 0 and vitorias % 5 == 0:
            print(c(f"\n  ⚠️  ATENÇÃO: Batalha de CHEFE!", Cor.VERMELHO + Cor.BOLD))
            pausa(0.5)

        venceu = batalha(jogador, vitorias)

        if not venceu:
            # Game Over
            print()
            titulo("💀  GAME OVER", Cor.VERMELHO)
            print(f"  Vitórias: {c(str(vitorias), Cor.AMARELO)}")
            print(f"  Nível alcançado: {c(str(jogador.nivel), Cor.CIANO)}")
            salvar_recorde(jogador.nome, jogador.classe, vitorias, jogador.nivel)
            print(c("\n  ✅ Recorde salvo!", Cor.VERDE))
            aguardar()
            return

        vitorias += 1
        jogador.vitorias = vitorias
        print(c(f"\n  🏆 Vitórias: {vitorias}", Cor.VERDE))
        pausa(1)

        # Entre batalhas
        continuar = entre_batalhas(jogador, vitorias)

        if not continuar:
            # Salvar e sair
            slot = menu_saves("salvar")
            if slot:
                caminho = salvar_jogo(jogador, vitorias, slot)
                print(c(f"\n  💾 Jogo salvo no slot {slot}!", Cor.VERDE))
            aguardar()
            return

        aguardar()


# ─── Entry point ─────────────────────────────────────────────────────────────
def main():
    while True:
        tela_titulo()
        opcao = tela_titulo()

        if opcao == "1":
            jogador, vitorias = novo_jogo()
            jogo_principal(jogador, vitorias)

        elif opcao == "2":
            slot = menu_saves("carregar")
            if slot:
                jogador, vitorias = carregar_jogo(slot)
                if jogador:
                    print(c(f"\n  ✅ Jogo carregado! Bem-vindo de volta, {jogador.nome}!", Cor.VERDE))
                    pausa(1)
                    jogo_principal(jogador, vitorias)
                else:
                    print(c("  ⚠️  Slot vazio!", Cor.VERMELHO))
                    pausa(1)

        elif opcao == "3":
            limpar_tela()
            mostrar_recordes()
            aguardar()

        elif opcao == "4":
            print(c("\n  Até logo, aventureiro! 👋\n", Cor.CIANO))
            sys.exit(0)


if __name__ == "__main__":
    main()
