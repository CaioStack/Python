# 1. Crie uma função chamada `eh_palindromo` que receba uma palavra e retorne `True` se ela for um palíndromo ou `False` caso contrário.

def eh_palindromo(palavra):
    # Converte para minúsculas para evitar diferenciação entre maiúsculas e minúsculas
    palavra_formatada = palavra.lower()
    
    # Compara a palavra com ela mesma invertida
    return palavra_formatada == palavra_formatada[::-1]


print(eh_palindromo("Arara"))  # Retorna True
print(eh_palindromo("Python")) # Retorna False