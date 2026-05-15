# Crie uma função chamada contar_caracteres que receba uma string como parâmetro e retorne a quantidade de caracteres dessa string sem usar a função len(). Depois, leia uma palavra do usuário, chame a função e mostre o resultado.

def contar_caracteres(texto):
    contador = 0
    for caractere in texto:
        contador += 1
    return contador


# Lê a palavra do usuário
palavra = input("Digite uma palavra: ")

# Chama a função e armazena o resultado
resultado = contar_caracteres(palavra)

# Mostra o resultado na tela
print(f"A palavra digitada possui {resultado} caracteres.")