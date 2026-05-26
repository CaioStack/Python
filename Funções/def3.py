# Crie uma função chamada conversor_moeda que recebe um valor
# em real brasileiro (BRL) e uma taxa de câmbio como argumentos
# e retorna o valor equivalente em dólares americanos (USD).
# Peça ao usuário para inserir o valor em BRL e a taxa de câmbio
# e exiba o valor correspondente em USD.

def conversor_moeda(valor_brl, taxa_cambio):
    return valor_brl / taxa_cambio

valor = float(input("Digite o valor em BRL (R$): "))
taxa = float(input("Digite a taxa de câmbio (ex: 5.20): "))

valor_usd = conversor_moeda(valor, taxa)
print(f"R$ {valor:.2f} equivale a US$ {valor_usd:.2f}")