# Crie uma função chamada fibonacci que gera a sequência de
# Fibonacci até o enésimo termo especificado pelo usuário.
# A sequência começa com 0 e 1, e cada termo subsequente é
# a soma dos dois termos anteriores.
# Peça ao usuário para inserir o número de termos que deseja
# na sequência e exiba a sequência resultante.

def fibonacci(n):
    sequencia = []
 
    if n == 1:
        sequencia.append(0)
    elif n >= 2:
        sequencia.append(0)
        sequencia.append(1)
        i = 2
        while i < n:
            proximo = sequencia[i - 1] + sequencia[i - 2]
            sequencia.append(proximo)
            i = i + 1
 
    return sequencia

termos = int(input("Quantos termos da sequência de Fibonacci deseja? "))
seq = fibonacci(termos)

print(f"Sequência de Fibonacci com {termos} termo(s):")
print(seq)