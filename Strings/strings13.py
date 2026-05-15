# 1. Crie uma função chamada `concatenar_fatiar` que receba duas strings como entrada.
# A função deve retornar uma nova string formada por:

# - Os três primeiros caracteres da primeira string
# - Os três últimos caracteres da segunda string

def concatenar_fatiar(str1, str2):
    tres_primeiros = str1[:3]
    tres_ultimos = str2[-3:]
    return tres_primeiros + tres_ultimos


palavra_a = input("Digite a primeira palavra: ")
palavra_b = input("Digite a segunda palavra: ")

resultado = concatenar_fatiar(palavra_a, palavra_b)
print(f"Resultado do fatiamento: {resultado}")