import random
from modules.ui import (c, Cor, negrito, barra_vida, barra_xp,
                         msg_dano, msg_nivel, adicionar_log, pausa)
from modules.itens import Inventario, Item

# ─── Habilidades ──────────────────────────────────────────────────────────────
HABILIDADES = {
    # Guerreiro
    "golpe_poderoso": {
        "nome": "Golpe Poderoso", "icone": "⚔️",
        "desc": "2.5x ataque, chance de atordoar",
        "cooldown": 3, "nivel_req": 1,
        "fn": lambda s, a: _golpe_poderoso(s, a)
    },
    "grito_guerra": {
        "nome": "Grito de Guerra", "icone": "📣",
        "desc": "+6 ataque por 3 turnos",
        "cooldown": 4, "nivel_req": 3,
        "fn": lambda s, a: _grito_guerra(s, a)
    },
    "provocar": {
        "nome": "Provocar", "icone": "😤",
        "desc": "Força inimigo a atacar, defesa +50%",
        "cooldown": 3, "nivel_req": 5,
        "fn": lambda s, a: _provocar(s, a)
    },
    # Mago
    "bola_fogo": {
        "nome": "Bola de Fogo", "icone": "🔥",
        "desc": "2x ataque + queimadura por 3 turnos",
        "cooldown": 2, "nivel_req": 1,
        "fn": lambda s, a: _bola_fogo(s, a)
    },
    "congelar": {
        "nome": "Congelar", "icone": "❄️",
        "desc": "1.5x ataque + paralisa inimigo",
        "cooldown": 3, "nivel_req": 3,
        "fn": lambda s, a: _congelar(s, a)
    },
    "canalizar": {
        "nome": "Canalizar Magia", "icone": "✨",
        "desc": "Cura 40% do HP máximo",
        "cooldown": 5, "nivel_req": 5,
        "fn": lambda s, a: _canalizar(s, a)
    },
    # Arqueiro
    "tiro_certeiro": {
        "nome": "Tiro Certeiro", "icone": "🎯",
        "desc": "Ignora defesa do inimigo, 1.8x ataque",
        "cooldown": 2, "nivel_req": 1,
        "fn": lambda s, a: _tiro_certeiro(s, a)
    },
    "chuva_flechas": {
        "nome": "Chuva de Flechas", "icone": "🏹",
        "desc": "3 ataques rápidos",
        "cooldown": 4, "nivel_req": 3,
        "fn": lambda s, a: _chuva_flechas(s, a)
    },
    "flecha_venenosa": {
        "nome": "Flecha Venenosa", "icone": "☠️",
        "desc": "1.2x ataque + veneno por 4 turnos",
        "cooldown": 3, "nivel_req": 5,
        "fn": lambda s, a: _flecha_venenosa(s, a)
    },
}

HABILIDADES_CLASSE = {
    "Guerreiro": ["golpe_poderoso", "grito_guerra", "provocar"],
    "Mago":      ["bola_fogo", "congelar", "canalizar"],
    "Arqueiro":  ["tiro_certeiro", "chuva_flechas", "flecha_venenosa"],
}

# ─── Implementações das habilidades ──────────────────────────────────────────
def _golpe_poderoso(self, alvo):
    dano = int(self.ataque * 2.5)
    alvo.receber_dano(dano, ignorar_defesa=False)
    print(f"  ⚔️  {c('Golpe Poderoso!', Cor.AMARELO)} — {c(str(dano), Cor.VERMELHO)} dano!")
    if random.random() < 0.3:
        alvo.aplicar_status("paralisia")
    adicionar_log(f"Golpe Poderoso: {dano} dano em {alvo.nome}")

def _grito_guerra(self, alvo):
    self.buff_ataque = (6, 3)
    self.ataque += 6
    print(f"  📣 {c('Grito de Guerra!', Cor.AMARELO)} +6 Ataque por 3 turnos!")
    adicionar_log("Grito de Guerra: +6 Ataque")

def _provocar(self, alvo):
    self.defendendo = True
    self.defesa_temp = int(self.defesa * 0.5)
    self.defesa += self.defesa_temp
    alvo.forcado_atacar = True
    print(f"  😤 {c('Provocação!', Cor.LARANJA)} Inimigo forçado a atacar. Defesa aumentada!")
    adicionar_log("Provocar: defesa +50%")

def _bola_fogo(self, alvo):
    dano = int(self.ataque * 2)
    alvo.receber_dano(dano)
    alvo.aplicar_status("queimadura")
    print(f"  🔥 {c('Bola de Fogo!', Cor.LARANJA)} {c(str(dano), Cor.VERMELHO)} dano + queimadura!")
    adicionar_log(f"Bola de Fogo: {dano} dano + queimadura")

def _congelar(self, alvo):
    dano = int(self.ataque * 1.5)
    alvo.receber_dano(dano)
    alvo.aplicar_status("paralisia")
    print(f"  ❄️  {c('Congelar!', Cor.AZUL)} {c(str(dano), Cor.VERMELHO)} dano + paralisia!")
    adicionar_log(f"Congelar: {dano} dano + paralisia")

def _canalizar(self, alvo):
    cura = int(self.vida_max * 0.4)
    self.vida = min(self.vida + cura, self.vida_max)
    print(f"  ✨ {c('Canalizar Magia!', Cor.CIANO)} Recuperou {c(str(cura), Cor.VERDE)} HP!")
    adicionar_log(f"Canalizar: +{cura} HP")

def _tiro_certeiro(self, alvo):
    dano = int(self.ataque * 1.8)
    alvo.vida -= max(0, dano)  # ignora defesa
    print(f"  🎯 {c('Tiro Certeiro!', Cor.VERDE)} {c(str(dano), Cor.VERMELHO)} dano (ignora defesa)!")
    adicionar_log(f"Tiro Certeiro: {dano} dano ignorando defesa")

def _chuva_flechas(self, alvo):
    total = 0
    for i in range(3):
        d = int(self.ataque * (0.6 + random.random() * 0.4))
        alvo.receber_dano(d)
        total += d
        pausa(0.2)
    print(f"  🏹 {c('Chuva de Flechas!', Cor.VERDE)} 3 flechas — {c(str(total), Cor.VERMELHO)} dano total!")
    adicionar_log(f"Chuva de Flechas: {total} dano total")

def _flecha_venenosa(self, alvo):
    dano = int(self.ataque * 1.2)
    alvo.receber_dano(dano)
    alvo.aplicar_status("veneno", turnos=4)
    print(f"  ☠️  {c('Flecha Venenosa!', Cor.MAGENTA)} {c(str(dano), Cor.VERMELHO)} dano + veneno!")
    adicionar_log(f"Flecha Venenosa: {dano} dano + veneno")

# ─── Classe Personagem ───────────────────────────────────────────────────────
class Personagem:
    def __init__(self, nome, vida, ataque, defesa, classe=None):
        self.nome = nome
        self.classe = classe or nome
        self.vida = vida
        self.vida_max = vida
        self.ataque = ataque
        self.ataque_base = ataque
        self.defesa = defesa
        self.defesa_base = defesa
        self.defendendo = False
        self.defesa_temp = 0
        self.forcado_atacar = False
        self.nivel = 1
        self.xp = 0
        self.ouro = 100
        self.vitorias = 0

        # Habilidades: {chave: cooldown_restante}
        self.habilidades_disponiveis = []
        self.cooldowns = {}

        # Status
        self.status_efeitos = {}  # {"veneno": turnos_restantes, ...}

        # Buffs temporários
        self.buff_ataque = None  # (valor, turnos)

        # Bônus especiais
        self.chance_critico = 15  # %
        self.chance_esquiva = 5   # %

        # Inventário
        self.inventario = Inventario()

        if classe:
            self._inicializar_habilidades(classe)

    def _inicializar_habilidades(self, classe):
        chaves = HABILIDADES_CLASSE.get(classe, [])
        self.habilidades_disponiveis = []
        for chave in chaves:
            h = HABILIDADES[chave]
            if h["nivel_req"] <= self.nivel:
                self.habilidades_disponiveis.append(chave)
                self.cooldowns[chave] = 0

    def _verificar_novas_habilidades(self):
        classe = self.classe
        chaves = HABILIDADES_CLASSE.get(classe, [])
        novas = []
        for chave in chaves:
            h = HABILIDADES[chave]
            if h["nivel_req"] <= self.nivel and chave not in self.habilidades_disponiveis:
                self.habilidades_disponiveis.append(chave)
                self.cooldowns[chave] = 0
                novas.append(h["nome"])
        return novas

    def atacar(self, alvo):
        critico = random.randint(1, 100) <= self.chance_critico
        variacao = random.randint(-3, 5)
        dano = self.ataque + variacao
        if critico:
            dano = int(dano * 2)
        alvo.receber_dano(dano)
        msg_dano(self.nome, dano, critico)
        adicionar_log(f"{self.nome} atacou {alvo.nome}: {dano} dano{'(CRÍTICO)' if critico else ''}")
        return dano

    def usar_habilidade(self, alvo, indice):
        if indice >= len(self.habilidades_disponiveis):
            return False
        chave = self.habilidades_disponiveis[indice]
        if self.cooldowns.get(chave, 0) > 0:
            print(c(f"  ⏳ {HABILIDADES[chave]['nome']} em recarga ({self.cooldowns[chave]} turnos)!", Cor.AMARELO))
            return False
        HABILIDADES[chave]["fn"](self, alvo)
        self.cooldowns[chave] = HABILIDADES[chave]["cooldown"]
        return True

    def defender(self):
        self.defendendo = True
        print(f"  🛡️  {c(self.nome, Cor.BRANCO)} está {c('defendendo!', Cor.AZUL)}")
        adicionar_log(f"{self.nome} defendeu")

    def receber_dano(self, dano, ignorar_defesa=False):
        # Esquiva
        if random.randint(1, 100) <= self.chance_esquiva:
            print(f"  💨 {c(self.nome, Cor.BRANCO)} {c('esquivou!', Cor.CIANO)}")
            adicionar_log(f"{self.nome} esquivou!")
            return 0

        if self.defendendo:
            dano = int(dano * 0.45)
            self.defendendo = False
            print(c("  🛡️  Dano reduzido pela defesa!", Cor.AZUL))

        if not ignorar_defesa:
            dano = max(1, dano - self.defesa)

        self.vida = max(0, self.vida - dano)
        return dano

    def aplicar_status(self, efeito, turnos=3):
        if efeito == "paralisia" and random.random() < 0.5:
            print(c(f"  ⚡ {self.nome} resistiu à paralisia!", Cor.AMARELO))
            return
        self.status_efeitos[efeito] = turnos
        icones = {"veneno": "☠️", "queimadura": "🔥", "paralisia": "⚡"}
        print(f"  {icones.get(efeito,'❓')} {c(self.nome, Cor.BRANCO)} está {c(efeito, Cor.MAGENTA)} ({turnos} turnos)!")
        adicionar_log(f"{self.nome} recebeu {efeito}")

    def processar_status(self):
        """Processa efeitos de turno — retorna True se ainda vivo."""
        removidos = []
        for efeito, turnos in list(self.status_efeitos.items()):
            if efeito == "veneno":
                dano = int(self.vida_max * 0.08)
                self.vida = max(0, self.vida - dano)
                print(f"  ☠️  {c(self.nome, Cor.MAGENTA)} perdeu {c(str(dano), Cor.VERMELHO)} HP por veneno!")
            elif efeito == "queimadura":
                dano = int(self.vida_max * 0.06)
                self.vida = max(0, self.vida - dano)
                print(f"  🔥 {c(self.nome, Cor.LARANJA)} perdeu {c(str(dano), Cor.VERMELHO)} HP por queimadura!")
            self.status_efeitos[efeito] = turnos - 1
            if self.status_efeitos[efeito] <= 0:
                removidos.append(efeito)
        for r in removidos:
            del self.status_efeitos[r]
            print(f"  ✅ {c(self.nome, Cor.BRANCO)} se recuperou de {c(r, Cor.CINZA)}.")
        return self.vida > 0

    def reduzir_cooldowns(self):
        for chave in self.cooldowns:
            if self.cooldowns[chave] > 0:
                self.cooldowns[chave] -= 1
        # Buff de ataque temporário
        if self.buff_ataque:
            valor, turnos = self.buff_ataque
            turnos -= 1
            if turnos <= 0:
                self.ataque -= valor
                self.buff_ataque = None
                print(c(f"  📉 Buff de ataque de {self.nome} expirou.", Cor.CINZA))
            else:
                self.buff_ataque = (valor, turnos)
        # Defesa temporária
        if self.defesa_temp > 0 and not self.defendendo:
            self.defesa -= self.defesa_temp
            self.defesa_temp = 0

    def ganhar_xp(self, quantidade):
        self.xp += quantidade
        print(f"  ⭐ +{c(str(quantidade), Cor.AMARELO)} XP!")
        while self.xp >= 50:
            self.xp -= 50
            self.subir_nivel()

    def subir_nivel(self):
        self.nivel += 1
        self.ataque_base += 2
        self.ataque += 2
        self.defesa_base += 1
        self.defesa += 1
        self.vida_max += 15
        self.vida = self.vida_max
        msg_nivel(self.nome, self.nivel)
        novas = self._verificar_novas_habilidades()
        for h in novas:
            print(f"  🆕 Nova habilidade desbloqueada: {c(h, Cor.CIANO)}!")

    def mostrar_status_completo(self):
        print(f"\n  {c(self.nome, Cor.BRANCO + Cor.BOLD)} — {c(self.classe, Cor.CIANO)} Nível {c(str(self.nivel), Cor.AMARELO)}")
        print(f"  HP:    {barra_vida(self.vida, self.vida_max)}")
        print(f"  XP:    {barra_xp(self.xp)}")
        print(f"  ATK: {c(str(self.ataque), Cor.VERMELHO)}  DEF: {c(str(self.defesa), Cor.AZUL)}  "
              f"CRIT: {c(str(self.chance_critico)+'%', Cor.AMARELO)}  ESQ: {c(str(self.chance_esquiva)+'%', Cor.VERDE)}")
        print(f"  💰 Ouro: {c(str(self.ouro), Cor.AMARELO)}  🏆 Vitórias: {c(str(self.vitorias), Cor.BRANCO)}")
        if self.status_efeitos:
            status_str = ", ".join([f"{k}({v}t)" for k, v in self.status_efeitos.items()])
            print(f"  Status: {c(status_str, Cor.MAGENTA)}")

    def esta_vivo(self):
        return self.vida > 0

# ─── Classe Inimigo ───────────────────────────────────────────────────────────
DADOS_INIMIGOS = {
    "Goblin":      {"vida": 70,  "ataque": 10, "defesa": 3,  "xp": 15, "ouro": (5,15),  "icone": "👺"},
    "Orc":         {"vida": 110, "ataque": 14, "defesa": 5,  "xp": 25, "ouro": (10,25), "icone": "👹"},
    "Troll":       {"vida": 140, "ataque": 16, "defesa": 8,  "xp": 35, "ouro": (15,30), "icone": "🧌"},
    "Lobo Sombrio":{"vida": 90,  "ataque": 18, "defesa": 4,  "xp": 30, "ouro": (8,20),  "icone": "🐺"},
    "Esqueleto":   {"vida": 80,  "ataque": 12, "defesa": 6,  "xp": 20, "ouro": (5,18),  "icone": "💀"},
    "Dragão":      {"vida": 200, "ataque": 24, "defesa": 12, "xp": 60, "ouro": (40,80), "icone": "🐉"},
}

CHEFES = {
    "Senhor das Trevas": {"vida": 300, "ataque": 28, "defesa": 15, "xp": 120, "ouro": (80,150), "icone": "👿"},
    "Lich Rei":          {"vida": 260, "ataque": 32, "defesa": 10, "xp": 110, "ouro": (70,130), "icone": "💀"},
    "Hidra Ancião":      {"vida": 350, "ataque": 22, "defesa": 18, "xp": 130, "ouro": (90,160), "icone": "🐲"},
}

class Inimigo(Personagem):
    def __init__(self, nome, vida, ataque, defesa, xp, ouro_range, icone, chefe=False):
        super().__init__(nome, vida, ataque, defesa)
        self.xp_recompensa = xp
        self.ouro_range = ouro_range
        self.icone = icone
        self.chefe = chefe
        self.fase = 1
        self.max_fases = 2 if chefe else 1

    def escolher_acao(self, alvo):
        # Paralisia impede ação
        if "paralisia" in self.status_efeitos:
            print(f"  ⚡ {c(self.nome, Cor.AMARELO)} está paralisado e perde o turno!")
            return

        if self.forcado_atacar:
            self.forcado_atacar = False
            self.atacar(alvo)
            return

        if self.chefe:
            self._acao_chefe(alvo)
        else:
            self._acao_normal(alvo)

    def _acao_normal(self, alvo):
        # Defende se com pouca vida
        if self.vida < self.vida_max * 0.25 and random.random() < 0.3:
            self.defender()
            return

        opcoes = ["ataque"] * 5 + ["especial"] * 2 + ["defesa"]
        acao = random.choice(opcoes)

        if acao == "ataque":
            self.atacar(alvo)
        elif acao == "especial":
            dano = int(self.ataque * 1.6 + random.randint(2, 8))
            alvo.receber_dano(dano)
            print(f"  🔥 {c(self.nome, Cor.LARANJA)} usou ataque especial: {c(str(dano), Cor.VERMELHO)} dano!")
            adicionar_log(f"{self.nome} ataque especial: {dano} dano")
            # Chance de aplicar status
            if random.random() < 0.2:
                alvo.aplicar_status(random.choice(["veneno", "queimadura"]))
        else:
            self.defender()

    def _acao_chefe(self, alvo):
        """Chefes têm padrões mais complexos."""
        # Fase 2 começa com 50% de vida
        if self.fase == 1 and self.vida < self.vida_max * 0.5:
            self.fase = 2
            print(f"\n  {c('💀 ' + self.nome + ' ENTROU NA FASE 2!', Cor.VERMELHO + Cor.BOLD)}")
            self.ataque = int(self.ataque * 1.3)
            pausa(1)

        opcoes_f1 = ["ataque", "ataque", "especial", "defesa"]
        opcoes_f2 = ["ataque", "ataque", "especial", "especial", "habilidade"]
        opcoes = opcoes_f2 if self.fase == 2 else opcoes_f1
        acao = random.choice(opcoes)

        if acao == "ataque":
            self.atacar(alvo)
        elif acao == "especial":
            dano = int(self.ataque * 2)
            alvo.receber_dano(dano)
            print(f"  🌑 {c(self.nome + ' — Ataque Sombrio!', Cor.ROXO)} {c(str(dano), Cor.VERMELHO)} dano!")
        elif acao == "habilidade":
            dano = int(self.ataque * 1.5)
            alvo.receber_dano(dano)
            alvo.aplicar_status(random.choice(["veneno", "queimadura", "paralisia"]))
            print(f"  💀 {c(self.nome + ' — Feitiço Maldito!', Cor.MAGENTA)}")
        else:
            self.defender()

    def droppar_ouro(self):
        return random.randint(*self.ouro_range)

def criar_inimigo(vitoria, forca_chefe=False):
    """Cria inimigo baseado na progressão."""
    if forca_chefe or vitoria > 0 and vitoria % 5 == 0:
        nome, dados = random.choice(list(CHEFES.items()))
        return Inimigo(nome, dados["vida"], dados["ataque"], dados["defesa"],
                       dados["xp"], dados["ouro"], dados["icone"], chefe=True)

    # Seleciona inimigos com base na vitória
    pool = ["Goblin", "Esqueleto"]
    if vitoria >= 2:
        pool += ["Orc", "Lobo Sombrio"]
    if vitoria >= 4:
        pool += ["Troll"]
    if vitoria >= 7:
        pool += ["Dragão"]

    nome = random.choice(pool)
    dados = DADOS_INIMIGOS[nome]
    # Escalar dificuldade
    escala = 1 + vitoria * 0.07
    return Inimigo(
        nome,
        int(dados["vida"] * escala),
        int(dados["ataque"] * escala),
        int(dados["defesa"] * escala),
        dados["xp"],
        dados["ouro"],
        dados["icone"]
    )

# ─── Escolher classe ──────────────────────────────────────────────────────────
CLASSES = {
    "guerreiro": {
        "nome": "Guerreiro", "icone": "⚔️",
        "vida": 130, "ataque": 16, "defesa": 12,
        "critico": 10, "esquiva": 5,
        "desc": "Tanque resistente. Ótima defesa e habilidades de controle."
    },
    "mago": {
        "nome": "Mago", "icone": "🧙",
        "vida": 85, "ataque": 24, "defesa": 5,
        "critico": 20, "esquiva": 8,
        "desc": "Alto dano e magia. Fraco fisicamente, letal a distância."
    },
    "arqueiro": {
        "nome": "Arqueiro", "icone": "🏹",
        "vida": 105, "ataque": 20, "defesa": 8,
        "critico": 25, "esquiva": 15,
        "desc": "Versátil e ágil. Alta chance de crítico e esquiva."
    },
}

def escolher_classe():
    from modules.ui import titulo, linha, c, Cor, prompt

    titulo("🧙 ESCOLHA SUA CLASSE", Cor.CIANO)
    for chave, dados in CLASSES.items():
        print(f"\n  {dados['icone']} {c(dados['nome'], Cor.AMARELO + Cor.BOLD)}")
        print(f"     {c(dados['desc'], Cor.CINZA)}")
        print(f"     HP: {c(str(dados['vida']), Cor.VERDE)}  "
              f"ATK: {c(str(dados['ataque']), Cor.VERMELHO)}  "
              f"DEF: {c(str(dados['defesa']), Cor.AZUL)}  "
              f"CRIT: {c(str(dados['critico'])+'%', Cor.AMARELO)}  "
              f"ESQ: {c(str(dados['esquiva'])+'%', Cor.CIANO)}")

    while True:
        linha()
        escolha = prompt("Classe (guerreiro/mago/arqueiro): ").lower()
        if escolha in CLASSES:
            d = CLASSES[escolha]
            p = Personagem(d["nome"], d["vida"], d["ataque"], d["defesa"], classe=d["nome"])
            p.chance_critico = d["critico"]
            p.chance_esquiva = d["esquiva"]
            # Iniciar com poção pequena
            p.inventario.adicionar(Item("pocao_pequena"))
            p.inventario.adicionar(Item("pocao_pequena"))
            return p
        print(c("  ⚠️  Classe inválida!", Cor.VERMELHO))
