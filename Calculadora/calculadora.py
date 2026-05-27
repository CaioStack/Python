"""
Calculadora completa para terminal em Python.
Suporta operações básicas, avançadas e histórico de cálculos.
"""

import math
import os

# ──────────────────────────────────────────────
# Funções de operações básicas
# ──────────────────────────────────────────────

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    # Evita divisão por zero
    if b == 0:
        raise ValueError("Erro: divisão por zero não é permitida.")
    return a / b

def resto(a, b):
    # Módulo (resto da divisão inteira)
    if b == 0:
        raise ValueError("Erro: divisão por zero não é permitida.")
    return a % b

def potencia(a, b):
    return a ** b

def raiz_quadrada(a):
    # Raiz quadrada só funciona para números não-negativos
    if a < 0:
        raise ValueError("Erro: raiz quadrada de número negativo.")
    return math.sqrt(a)

def logaritmo(a, base=10):
    # Logaritmo só é definido para valores positivos
    if a <= 0:
        raise ValueError("Erro: logaritmo de número não-positivo.")
    if base <= 0 or base == 1:
        raise ValueError("Erro: base inválida para logaritmo.")
    return math.log(a, base)

def seno(a):
    # Recebe o ângulo em graus e converte para radianos
    return math.sin(math.radians(a))

def cosseno(a):
    return math.cos(math.radians(a))

def tangente(a):
    return math.tan(math.radians(a))

def fatorial(a):
    # Fatorial só existe para inteiros não-negativos
    if a < 0 or not float(a).is_integer():
        raise ValueError("Erro: fatorial requer inteiro não-negativo.")
    return math.factorial(int(a))

# ──────────────────────────────────────────────
# Utilitários de interface
# ──────────────────────────────────────────────

def limpar_tela():
    # Funciona tanto no Windows quanto no Linux/Mac
    os.system("cls" if os.name == "nt" else "clear")

def exibir_cabecalho():
    print("=" * 42)
    print("        CALCULADORA COMPLETA v1.0")
    print("         by.Caio Salgado Marques")
    print("=" * 42)

def exibir_menu():
    """Exibe o menu de opções para o usuário."""
    print("\n── Operações Básicas ──────────────────")
    print("  1  Adição             (a + b)")
    print("  2  Subtração          (a - b)")
    print("  3  Multiplicação      (a × b)")
    print("  4  Divisão            (a ÷ b)")
    print("  5  Resto da divisão   (a % b)")
    print("  6  Potência           (a ^ b)")
    print("\n── Operações Avançadas ────────────────")
    print("  7  Raiz quadrada      (√a)")
    print("  8  Logaritmo          (log_base(a))")
    print("  9  Seno               (sen(°))")
    print(" 10  Cosseno            (cos(°))")
    print(" 11  Tangente           (tan(°))")
    print(" 12  Fatorial           (n!)")
    print("\n── Extras ─────────────────────────────")
    print(" 13  Ver histórico")
    print(" 14  Limpar histórico")
    print("  0  Sair")
    print("─" * 42)

def ler_numero(mensagem):
    """Lê e valida um número digitado pelo usuário."""
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        try:
            return float(entrada)
        except ValueError:
            print("  ⚠  Digite um número válido.")

def formatar_resultado(valor):
    """
    Exibe inteiros sem casas decimais e floats com até 10 casas.
    Remove zeros desnecessários no final.
    """
    if isinstance(valor, float) and valor.is_integer():
        return str(int(valor))
    return f"{valor:.10g}"

# ──────────────────────────────────────────────
# Lógica principal
# ──────────────────────────────────────────────

def executar_operacao(opcao, historico):
    """
    Executa a operação escolhida, exibe o resultado
    e salva no histórico.
    """
    resultado = None
    expressao = ""

    try:
        # Operações que precisam de dois números
        if opcao in (1, 2, 3, 4, 5, 6):
            a = ler_numero("  Primeiro número : ")
            b = ler_numero("  Segundo número  : ")

            if opcao == 1:
                resultado = somar(a, b)
                expressao = f"{formatar_resultado(a)} + {formatar_resultado(b)}"
            elif opcao == 2:
                resultado = subtrair(a, b)
                expressao = f"{formatar_resultado(a)} - {formatar_resultado(b)}"
            elif opcao == 3:
                resultado = multiplicar(a, b)
                expressao = f"{formatar_resultado(a)} × {formatar_resultado(b)}"
            elif opcao == 4:
                resultado = dividir(a, b)
                expressao = f"{formatar_resultado(a)} ÷ {formatar_resultado(b)}"
            elif opcao == 5:
                resultado = resto(a, b)
                expressao = f"{formatar_resultado(a)} % {formatar_resultado(b)}"
            elif opcao == 6:
                resultado = potencia(a, b)
                expressao = f"{formatar_resultado(a)} ^ {formatar_resultado(b)}"

        # Operações que precisam de um número
        elif opcao == 7:
            a = ler_numero("  Número          : ")
            resultado = raiz_quadrada(a)
            expressao = f"√{formatar_resultado(a)}"

        elif opcao == 8:
            a = ler_numero("  Número          : ")
            base = ler_numero("  Base (padrão 10): ")
            resultado = logaritmo(a, base)
            expressao = f"log_{formatar_resultado(base)}({formatar_resultado(a)})"

        elif opcao in (9, 10, 11):
            a = ler_numero("  Ângulo (graus)  : ")
            if opcao == 9:
                resultado = seno(a)
                expressao = f"sen({formatar_resultado(a)}°)"
            elif opcao == 10:
                resultado = cosseno(a)
                expressao = f"cos({formatar_resultado(a)}°)"
            elif opcao == 11:
                resultado = tangente(a)
                expressao = f"tan({formatar_resultado(a)}°)"

        elif opcao == 12:
            a = ler_numero("  Número inteiro  : ")
            resultado = fatorial(a)
            expressao = f"{int(a)}!"

        # Exibe e salva o resultado
        if resultado is not None:
            print(f"\n  ✔  {expressao} = {formatar_resultado(resultado)}")
            historico.append(f"{expressao} = {formatar_resultado(resultado)}")

    except ValueError as e:
        # Captura erros matemáticos (ex: divisão por zero)
        print(f"\n  {e}")

def exibir_historico(historico):
    """Mostra todos os cálculos realizados na sessão."""
    print("\n── Histórico de cálculos ──────────────")
    if not historico:
        print("  (nenhum cálculo realizado ainda)")
    else:
        for i, entrada in enumerate(historico, 1):
            print(f"  {i:>3}. {entrada}")
    print("─" * 42)

def main():
    historico = []  # Lista que guarda os cálculos da sessão

    limpar_tela()
    exibir_cabecalho()

    while True:
        exibir_menu()
        entrada = input("  Escolha uma opção: ").strip()

        # Valida se a entrada é um número inteiro
        if not entrada.isdigit():
            print("  ⚠  Opção inválida. Digite um número do menu.")
            continue

        opcao = int(entrada)

        if opcao == 0:
            print("\n  Até logo! 👋\n")
            break
        elif opcao == 13:
            exibir_historico(historico)
        elif opcao == 14:
            historico.clear()
            print("  ✔  Histórico apagado.")
        elif 1 <= opcao <= 12:
            executar_operacao(opcao, historico)
        else:
            print("  ⚠  Opção inválida. Escolha entre 0 e 14.")

        input("\n  [Enter] para continuar...")
        limpar_tela()
        exibir_cabecalho()

# Ponto de entrada do programa
if __name__ == "__main__":
    main()