import json
import os
from datetime import datetime

PASTA_SAVES = os.path.join(os.path.dirname(__file__), "..", "saves")
ARQUIVO_RECORDES = os.path.join(PASTA_SAVES, "recordes.json")

os.makedirs(PASTA_SAVES, exist_ok=True)

def salvar_jogo(jogador, vitorias, slot=1):
    dados = {
        "nome": jogador.nome,
        "classe": jogador.classe,
        "vida": jogador.vida,
        "vida_max": jogador.vida_max,
        "ataque": jogador.ataque,
        "ataque_base": jogador.ataque_base,
        "defesa": jogador.defesa,
        "defesa_base": jogador.defesa_base,
        "nivel": jogador.nivel,
        "xp": jogador.xp,
        "ouro": jogador.ouro,
        "vitorias": vitorias,
        "chance_critico": jogador.chance_critico,
        "chance_esquiva": jogador.chance_esquiva,
        "habilidades": jogador.habilidades_disponiveis,
        "cooldowns": jogador.cooldowns,
        "inventario": [i.chave for i in jogador.inventario.itens],
        "equipamentos": {k: (v.chave if v else None) for k, v in jogador.inventario.equipamentos.items()},
        "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
    }
    caminho = os.path.join(PASTA_SAVES, f"save_{slot}.json")
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)
    return caminho

def carregar_jogo(slot=1):
    from modules.personagens import Personagem, HABILIDADES_CLASSE
    from modules.itens import Item, _aplicar_efeitos_equipamento

    caminho = os.path.join(PASTA_SAVES, f"save_{slot}.json")
    if not os.path.exists(caminho):
        return None, None

    with open(caminho, encoding="utf-8") as f:
        d = json.load(f)

    jogador = Personagem(d["nome"], d["vida_max"], d["ataque_base"], d["defesa_base"], classe=d["classe"])
    jogador.vida = d["vida"]
    jogador.ataque = d["ataque"]
    jogador.defesa = d["defesa"]
    jogador.nivel = d["nivel"]
    jogador.xp = d["xp"]
    jogador.ouro = d["ouro"]
    jogador.chance_critico = d["chance_critico"]
    jogador.chance_esquiva = d["chance_esquiva"]
    jogador.habilidades_disponiveis = d["habilidades"]
    jogador.cooldowns = d["cooldowns"]

    for chave in d["inventario"]:
        try:
            jogador.inventario.itens.append(Item(chave))
        except Exception:
            pass

    for slot_eq, chave in d["equipamentos"].items():
        if chave:
            try:
                item = Item(chave)
                jogador.inventario.equipamentos[slot_eq] = item
                _aplicar_efeitos_equipamento(jogador, item)
            except Exception:
                pass

    return jogador, d["vitorias"]

def listar_saves():
    saves = []
    for i in range(1, 4):
        caminho = os.path.join(PASTA_SAVES, f"save_{i}.json")
        if os.path.exists(caminho):
            with open(caminho, encoding="utf-8") as f:
                d = json.load(f)
            saves.append((i, d))
        else:
            saves.append((i, None))
    return saves

def salvar_recorde(nome, classe, vitorias, nivel):
    recordes = []
    if os.path.exists(ARQUIVO_RECORDES):
        with open(ARQUIVO_RECORDES, encoding="utf-8") as f:
            recordes = json.load(f)

    recordes.append({
        "nome": nome, "classe": classe,
        "vitorias": vitorias, "nivel": nivel,
        "data": datetime.now().strftime("%d/%m/%Y %H:%M")
    })
    recordes.sort(key=lambda x: x["vitorias"], reverse=True)
    recordes = recordes[:10]  # Top 10

    with open(ARQUIVO_RECORDES, "w", encoding="utf-8") as f:
        json.dump(recordes, f, ensure_ascii=False, indent=2)

def mostrar_recordes():
    from modules.ui import c, Cor, titulo, linha
    titulo("🏆 HALL DA FAMA", Cor.AMARELO)
    if not os.path.exists(ARQUIVO_RECORDES):
        print(c("  Nenhum recorde ainda!", Cor.CINZA))
        return

    with open(ARQUIVO_RECORDES, encoding="utf-8") as f:
        recordes = json.load(f)

    if not recordes:
        print(c("  Nenhum recorde ainda!", Cor.CINZA))
        return

    medalhas = ["🥇", "🥈", "🥉"]
    for i, r in enumerate(recordes):
        medalha = medalhas[i] if i < 3 else f"  {i+1}."
        print(f"  {medalha} {c(r['nome'], Cor.BRANCO)} ({c(r['classe'], Cor.CIANO)}) — "
              f"{c(str(r['vitorias']), Cor.AMARELO)} vitórias  Nível {c(str(r['nivel']), Cor.VERDE)}  {c(r['data'], Cor.CINZA)}")
    linha()
