# Crie uma função chamada calculadora que recebe dois números
# e o nome de uma operação ("soma", "subtracao", "multiplicacao",
# "divisao") como argumentos e retorna o resultado da operação.
# Peça ao usuário para inserir os números e a operação e exiba o resultado.

def calculadora(numero1, numero2, operacao):
    if operacao == "soma":
        return numero1 + numero2
    elif operacao == "subtracao":
        return numero1 - numero2
    elif operacao == "multiplicacao":
        return numero1 * numero2
    elif operacao == "divisao":
        if numero2 == 0:
            return "Erro: divisão por zero!"
        return numero1 / numero2
    else:
        return "Operação inválida!"

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
op = input("Digite a operação (soma, subtracao, multiplicacao, divisao): ")

resultado = calculadora(n1, n2, op)
print(f"Resultado: {resultado}")