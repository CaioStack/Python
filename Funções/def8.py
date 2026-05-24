# Crie uma função chamada contar_digitos que recebe um número
# inteiro como argumento e retorna a quantidade de dígitos
# no número. Peça ao usuário para inserir um número e exiba
# a quantidade de dígitos.

def contar_digitos(numero):
    if numero < 0:
        numero = numero * -1  # transforma em positivo
    if numero == 0:
        return 1
    contagem = 0
    while numero > 0:
        numero = numero // 10
        contagem = contagem + 1
    return contagem

num_digitos = int(input("Digite um número inteiro: "))
qtd = contar_digitos(num_digitos)
print(f"O número possui {qtd} dígito(s)")