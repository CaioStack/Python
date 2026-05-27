# =============================================================
# ESTRUTURAS CONDICIONAIS
# =============================================================
# Permitem que o programa tome decisões: "SE isso acontecer,
# faça aquilo; SENÃO, faça outra coisa."

# -------------------------------------------------------------
# IF SIMPLES
# -------------------------------------------------------------
# Executa o bloco apenas se a condição for True.
# ATENÇÃO: indentação (4 espaços) é obrigatória em Python!

temperatura = 35

if temperatura > 30:
    print("Está muito quente hoje!")
    print("Beba bastante água.")

# -------------------------------------------------------------
# IF / ELSE
# -------------------------------------------------------------
# O bloco else é executado quando a condição é False.

nota = 6.5

if nota >= 7:
    print("Aprovado!")
else:
    print("Reprovado.")

# -------------------------------------------------------------
# IF / ELIF / ELSE
# -------------------------------------------------------------
# elif ("else if") testa múltiplas condições em sequência.
# Apenas o PRIMEIRO bloco verdadeiro é executado.

media = 8.2

if media >= 9:
    print("Conceito A - Excelente!")
elif media >= 7:
    print("Conceito B - Bom!")
elif media >= 5:
    print("Conceito C - Regular.")
else:
    print("Conceito D - Insuficiente.")

# -------------------------------------------------------------
# CONDICIONAIS ANINHADAS
# -------------------------------------------------------------
# Um if dentro de outro if.

idade = 20
tem_documento = True

if idade >= 18:
    if tem_documento:
        print("Acesso liberado.")
    else:
        print("Precisa de documento.")
else:
    print("Menor de idade. Acesso negado.")

# -------------------------------------------------------------
# OPERADOR TERNÁRIO (if em uma linha)
# -------------------------------------------------------------
# Sintaxe: valor_se_true if condição else valor_se_false

numero = 7
paridade = "par" if numero % 2 == 0 else "ímpar"
print(f"O número {numero} é {paridade}.")

# -------------------------------------------------------------
# MATCH / CASE (Python 3.10+)
# -------------------------------------------------------------
# Similar ao switch de outras linguagens.

dia = 3

match dia:
    case 1:
        print("Segunda-feira")
    case 2:
        print("Terça-feira")
    case 3:
        print("Quarta-feira")
    case 4:
        print("Quinta-feira")
    case 5:
        print("Sexta-feira")
    case _:        # _ é o "padrão" (como o else)
        print("Final de semana!")

# -------------------------------------------------------------
# VERIFICAÇÕES ÚTEIS
# -------------------------------------------------------------

valor = None
lista = []
texto = ""

# Valores "falsy" em Python: None, 0, "", [], {}, ()
if not valor:
    print("valor está vazio ou None")

if not lista:
    print("lista está vazia")

# Verificando múltiplas opções com "in"
cor = "verde"
if cor in ["vermelho", "verde", "azul"]:
    print(f"{cor} é uma cor primária da luz RGB.")