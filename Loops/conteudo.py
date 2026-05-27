# =============================================================
# LOOPS (LAÇOS DE REPETIÇÃO)
# =============================================================
# Loops executam um bloco de código várias vezes, enquanto
# uma condição for verdadeira ou percorrendo uma sequência.

# -------------------------------------------------------------
# FOR — percorre uma sequência
# -------------------------------------------------------------
# Ideal quando sabemos quantas vezes queremos repetir.

# Percorrendo uma lista
frutas = ["maçã", "banana", "laranja", "uva"]
for fruta in frutas:
    print(f"Fruta: {fruta}")

# Percorrendo uma string (caractere por caractere)
for letra in "Python":
    print(letra, end=" ")  # end=" " evita quebra de linha
print()  # pula uma linha

# -------------------------------------------------------------
# RANGE — gerando sequências de números
# -------------------------------------------------------------
# range(stop)           → de 0 até stop-1
# range(start, stop)    → de start até stop-1
# range(start, stop, step) → com passo personalizado

for i in range(5):           # 0, 1, 2, 3, 4
    print(i, end=" ")
print()

for i in range(1, 6):        # 1, 2, 3, 4, 5
    print(i, end=" ")
print()

for i in range(0, 11, 2):    # 0, 2, 4, 6, 8, 10
    print(i, end=" ")
print()

for i in range(10, 0, -1):   # contagem regressiva: 10, 9, 8...
    print(i, end=" ")
print()

# -------------------------------------------------------------
# WHILE — repete enquanto a condição for True
# -------------------------------------------------------------
# Ideal quando não sabemos ao certo quantas repetições serão.

contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1  # IMPORTANTE: sempre avançar para evitar loop infinito

# Exemplo prático: adivinhar um número
# (descomente para testar interativamente)
# numero_secreto = 7
# while True:
#     tentativa = int(input("Adivinhe o número: "))
#     if tentativa == numero_secreto:
#         print("Acertou!")
#         break
#     elif tentativa < numero_secreto:
#         print("Tente um número maior.")
#     else:
#         print("Tente um número menor.")

# -------------------------------------------------------------
# BREAK — interrompe o loop imediatamente
# -------------------------------------------------------------

for i in range(10):
    if i == 5:
        print("Encontrei o 5! Parando...")
        break
    print(i, end=" ")
print()

# -------------------------------------------------------------
# CONTINUE — pula para a próxima iteração
# -------------------------------------------------------------

for i in range(10):
    if i % 2 == 0:
        continue   # pula os pares
    print(i, end=" ")  # exibe só os ímpares
print()

# -------------------------------------------------------------
# ELSE NO LOOP
# -------------------------------------------------------------
# O bloco else é executado quando o loop termina normalmente
# (sem break).

for i in range(5):
    print(i, end=" ")
else:
    print("\nLoop concluído sem interrupções.")

# -------------------------------------------------------------
# ENUMERATE — índice + valor ao mesmo tempo
# -------------------------------------------------------------

times = ["Flamengo", "Palmeiras", "Grêmio"]
for indice, time in enumerate(times, start=1):
    print(f"{indice}º lugar: {time}")

# -------------------------------------------------------------
# ZIP — percorrendo duas listas ao mesmo tempo
# -------------------------------------------------------------

nomes = ["Ana", "Bruno", "Carla"]
notas = [8.5, 7.0, 9.2]

for nome, nota in zip(nomes, notas):
    print(f"{nome}: {nota}")

# -------------------------------------------------------------
# LIST COMPREHENSION — criando listas com for em uma linha
# -------------------------------------------------------------
# Sintaxe: [expressão for item in sequência if condição]

quadrados = [x**2 for x in range(1, 6)]
print(quadrados)  # [1, 4, 9, 16, 25]

pares = [x for x in range(20) if x % 2 == 0]
print(pares)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]