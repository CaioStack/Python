# Considere a função criada na questão anterior (def6.py) e crie outra
# função chamada binomio que calcula o coeficiente binomial
# C(n, p) usando a função fatorial.
# Peça ao usuário para inserir dois números inteiros n e p
# e calcule o coeficiente binomial.

def fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    resultado = 1
    i = 2
    while i <= numero:
        resultado = resultado * i
        i = i + 1
    return resultado

def binomio(n, p):
    if p > n:
        return "p não pode ser maior que n!"
    return fatorial(n) // (fatorial(p) * fatorial(n - p))

n = int(input("Digite o valor de n: "))
p = int(input("Digite o valor de p: "))

resultado_binomio = binomio(n, p)
print(f"C({n}, {p}) = {resultado_binomio}")