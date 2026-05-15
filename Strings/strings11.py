# Crie uma função chamada inverter_texto que receba uma string como parâmetro e retorne essa string invertida.

def inverter_texto(texto):
    return texto[::-1]


palavra_original = input("Digite um texto para inverter: ")
palavra_invertida = inverter_texto(palavra_original)

print(f"Texto invertido: {palavra_invertida}")