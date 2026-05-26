import random
from modules.ui import c, Cor, negrito, linha, digitar, adicionar_log

# ─── Definições de itens ──────────────────────────────────────────────────────
ITENS = {
    # Poções
    "pocao_pequena": {
        "nome": "Poção Pequena", "tipo": "consumivel", "icone": "🧪",
        "desc": "Restaura 30 HP", "preco": 15,
        "efeito": {"cura": 30}
    },
    "pocao_grande": {
        "nome": "Poção Grande", "tipo": "consumivel", "icone": "⚗️",
        "desc": "Restaura 70 HP", "preco": 35,
        "efeito": {"cura": 70}
    },
    "pocao_vida": {
        "nome": "Elixir de Vida", "tipo": "consumivel", "icone": "💊",
        "desc": "Restaura HP totalmente", "preco": 80,
        "efeito": {"cura": 9999}
    },
    "antidoto": {
        "nome": "Antídoto", "tipo": "consumivel", "icone": "💉",
        "desc": "Cura veneno e queimadura", "preco": 20,
        "efeito": {"limpar_status": True}
    },
    "bomba_fogo": {
        "nome": "Bomba de Fogo", "tipo": "consumivel", "icone": "💣",
        "desc": "Causa 40 dano e queimadura", "preco": 30,
        "efeito": {"dano": 40, "status": "queimadura"}
    },
    # Equipamentos
    "espada_longa": {
        "nome": "Espada Longa", "tipo": "arma", "icone": "⚔️",
        "desc": "+8 Ataque", "preco": 50,
        "efeito": {"ataque": 8}
    },
    "machado_guerra": {
        "nome": "Machado de Guerra", "tipo": "arma", "icone": "🪓",
        "desc": "+14 Ataque, -3 Defesa", "preco": 70,
        "efeito": {"ataque": 14, "defesa": -3}
    },
    "cajado_magico": {
        "nome": "Cajado Mágico", "tipo": "arma", "icone": "🪄",
        "desc": "+6 Ataque, +10% crítico", "preco": 60,
        "efeito": {"ataque": 6, "critico_bonus": 10}
    },
    "escudo_aco": {
        "nome": "Escudo de Aço", "tipo": "armadura", "icone": "🛡️",
        "desc": "+8 Defesa", "preco": 45,
        "efeito": {"defesa": 8}
    },
    "armadura_couro": {
        "nome": "Armadura de Couro", "tipo": "armadura", "icone": "🥋",
        "desc": "+5 Defesa, +10 HP", "preco": 40,
        "efeito": {"defesa": 5, "vida_max": 10}
    },
    "manto_sombra": {
        "nome": "Manto das Sombras", "tipo": "armadura", "icone": "🧥",
        "desc": "+3 Defesa, +15% esquiva", "preco": 55,
        "efeito": {"defesa": 3, "esquiva_bonus": 15}
    },
    "amuleto_forca": {
        "nome": "Amuleto da Força", "tipo": "acessorio", "icone": "📿",
        "desc": "+5 Ataque, +5 Defesa", "preco": 65,
        "efeito": {"ataque": 5, "defesa": 5}
    },
}

# ─── Classe Item ──────────────────────────────────────────────────────────────
class Item:
    def __init__(self, chave):
        dados = ITENS[chave]
        self.chave = chave
        self.nome = dados["nome"]
        self.tipo = dados["tipo"]
        self.icone = dados["icone"]
        self.desc = dados["desc"]
        self.preco = dados["preco"]
        self.efeito = dados["efeito"]

    def __str__(self):
        return f"{self.icone} {self.nome}"

# ─── Inventário ───────────────────────────────────────────────────────────────
class Inventario:
    LIMITE = 12

    def __init__(self):
        self.itens = []
        self.equipamentos = {"arma": None, "armadura": None, "acessorio": None}

    def adicionar(self, item):
        if len(self.itens) >= self.LIMITE:
            print(c("  ⚠️  Inventário cheio!", Cor.VERMELHO))
            return False
        self.itens.append(item)
        return True

    def remover(self, indice):
        if 0 <= indice < len(self.itens):
            return self.itens.pop(indice)
        return None

    def mostrar(self, so_consumiveis=False):
        consumiveis = [i for i in self.itens if i.tipo == "consumivel"]
        equipamentos = [i for i in self.itens if i.tipo != "consumivel"]

        if so_consumiveis:
            lista = consumiveis
        else:
            lista = self.itens

        if not lista:
            print(c("  (vazio)", Cor.CINZA))
            return

        for idx, item in enumerate(lista):
            print(f"  {c(str(idx+1), Cor.AMARELO)}. {item} — {c(item.desc, Cor.CINZA)}")

    def mostrar_equipados(self):
        print(c("  Equipamentos ativos:", Cor.AZUL))
        slots = {"arma": "⚔️ Arma", "armadura": "🛡 Armadura", "acessorio": "📿 Acessório"}
        for slot, label in slots.items():
            eq = self.equipamentos[slot]
            val = str(eq) if eq else c("(vazio)", Cor.CINZA)
            print(f"    {label}: {val}")

    def consumiveis(self):
        return [i for i in self.itens if i.tipo == "consumivel"]

    def num_consumiveis(self):
        return len(self.consumiveis())

# ─── Usar item ────────────────────────────────────────────────────────────────
def usar_item(personagem, inventario, inimigo=None):
    consumiveis = inventario.consumiveis()
    if not consumiveis:
        print(c("  ⚠️  Sem consumíveis no inventário!", Cor.VERMELHO))
        return False

    linha()
    print(c("  🎒 Consumíveis disponíveis:", Cor.CIANO))
    for idx, item in enumerate(consumiveis):
        print(f"  {c(str(idx+1), Cor.AMARELO)}. {item} — {c(item.desc, Cor.CINZA)}")
    print(f"  {c('0', Cor.CINZA)}. Cancelar")

    try:
        escolha = int(input(c("  >>> ", Cor.CIANO))) - 1
    except ValueError:
        return False

    if escolha < 0 or escolha >= len(consumiveis):
        return False

    item = consumiveis[escolha]
    efeito = item.efeito

    usado = True
    if "cura" in efeito:
        cura = min(efeito["cura"], personagem.vida_max - personagem.vida)
        personagem.vida += cura
        print(f"  ✨ {c(item.nome, Cor.BRANCO)}: recuperou {c(str(cura), Cor.VERDE)} HP!")
        adicionar_log(f"{item.nome}: +{cura} HP para {personagem.nome}")

    if "limpar_status" in efeito:
        personagem.status_efeitos.clear()
        print(f"  💉 {c('Status negativos removidos!', Cor.VERDE)}")

    if "dano" in efeito and inimigo:
        dano = efeito["dano"]
        inimigo.receber_dano(dano)
        print(f"  💣 {c(item.nome, Cor.BRANCO)}: causou {c(str(dano), Cor.VERMELHO)} dano ao {inimigo.nome}!")
        if "status" in efeito:
            inimigo.aplicar_status(efeito["status"])
        adicionar_log(f"{item.nome}: {dano} dano em {inimigo.nome}")

    if usado:
        inventario.itens.remove(item)

    return usado

# ─── Equipar item ─────────────────────────────────────────────────────────────
def equipar_item(personagem, inventario):
    equipaveis = [i for i in inventario.itens if i.tipo in ("arma", "armadura", "acessorio")]
    if not equipaveis:
        print(c("  ⚠️  Sem equipamentos no inventário!", Cor.VERMELHO))
        return

    linha()
    print(c("  ⚔️  Equipamentos disponíveis:", Cor.CIANO))
    for idx, item in enumerate(equipaveis):
        print(f"  {c(str(idx+1), Cor.AMARELO)}. {item} — {c(item.desc, Cor.CINZA)}")
    print(f"  {c('0', Cor.CINZA)}. Cancelar")

    try:
        escolha = int(input(c("  >>> ", Cor.CIANO))) - 1
    except ValueError:
        return

    if escolha < 0 or escolha >= len(equipaveis):
        return

    item = equipaveis[escolha]
    slot = item.tipo

    # Desequipar anterior
    anterior = inventario.equipamentos[slot]
    if anterior:
        _remover_efeitos_equipamento(personagem, anterior)
        inventario.itens.append(anterior)
        print(f"  🔄 {c(str(anterior), Cor.CINZA)} desequipado.")

    # Equipar novo
    inventario.equipamentos[slot] = item
    inventario.itens.remove(item)
    _aplicar_efeitos_equipamento(personagem, item)
    print(f"  ✅ {c(str(item), Cor.VERDE)} equipado!")

def _aplicar_efeitos_equipamento(personagem, item):
    e = item.efeito
    if "ataque" in e:
        personagem.ataque_base += e["ataque"]
        personagem.ataque += e["ataque"]
    if "defesa" in e:
        personagem.defesa_base += e["defesa"]
        personagem.defesa += e["defesa"]
    if "vida_max" in e:
        personagem.vida_max += e["vida_max"]
        personagem.vida += e["vida_max"]
    if "critico_bonus" in e:
        personagem.chance_critico += e["critico_bonus"]
    if "esquiva_bonus" in e:
        personagem.chance_esquiva += e["esquiva_bonus"]

def _remover_efeitos_equipamento(personagem, item):
    e = item.efeito
    if "ataque" in e:
        personagem.ataque_base -= e["ataque"]
        personagem.ataque -= e["ataque"]
    if "defesa" in e:
        personagem.defesa_base -= e["defesa"]
        personagem.defesa -= e["defesa"]
    if "vida_max" in e:
        personagem.vida_max -= e["vida_max"]
        personagem.vida = min(personagem.vida, personagem.vida_max)
    if "critico_bonus" in e:
        personagem.chance_critico -= e["critico_bonus"]
    if "esquiva_bonus" in e:
        personagem.chance_esquiva -= e["esquiva_bonus"]

# ─── Loja ────────────────────────────────────────────────────────────────────
LOJA_ITENS = [
    "pocao_pequena", "pocao_grande", "pocao_vida",
    "antidoto", "bomba_fogo",
    "espada_longa", "machado_guerra", "cajado_magico",
    "escudo_aco", "armadura_couro", "manto_sombra",
    "amuleto_forca"
]

def abrir_loja(jogador):
    from modules.ui import titulo, prompt, linha, c, Cor
    titulo("⚗️  LOJA DO AVENTUREIRO", Cor.AMARELO)
    print(f"  {c('Ouro disponível:', Cor.AMARELO)} {c(str(jogador.ouro), Cor.BRANCO)} 💰\n")

    itens_disponiveis = [Item(k) for k in LOJA_ITENS]

    while True:
        linha()
        print(c("  CATÁLOGO:", Cor.CIANO))
        for idx, item in enumerate(itens_disponiveis):
            print(f"  {c(str(idx+1), Cor.AMARELO)}. {item} — {c(item.desc, Cor.CINZA)} | {c(str(item.preco)+'💰', Cor.AMARELO)}")
        print(f"\n  {c('V', Cor.VERDE)}. Ver inventário   {c('S', Cor.VERMELHO)}. Sair da loja")

        escolha = input(c("\n  Comprar (#) ou ação: ", Cor.CIANO)).strip().lower()

        if escolha == "s":
            break
        elif escolha == "v":
            linha()
            print(c("  🎒 Seu inventário:", Cor.CIANO))
            jogador.inventario.mostrar()
            continue

        try:
            idx = int(escolha) - 1
            item = itens_disponiveis[idx]
        except (ValueError, IndexError):
            print(c("  ⚠️  Opção inválida!", Cor.VERMELHO))
            continue

        if jogador.ouro < item.preco:
            print(c("  ❌ Ouro insuficiente!", Cor.VERMELHO))
        elif jogador.inventario.adicionar(item):
            jogador.ouro -= item.preco
            print(f"  ✅ {c(str(item), Cor.VERDE)} comprado! Ouro restante: {c(str(jogador.ouro), Cor.AMARELO)} 💰")
