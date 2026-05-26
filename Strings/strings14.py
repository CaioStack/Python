# Crie um programa que leia o nome e o sobrenome de uma pessoa. Depois, crie uma função chamada `gerar_usuario` que retorne um nome de usuário formado por:

# - As três primeiras letras do nome
# - As três últimas letras do sobrenome
# - Tudo em letras minúsculas

def gerar_usuario(nome, sobrenome):
    inicio_nome = nome[:3]
    
    fim_sobrenome = sobrenome[-3:]
    
    usuario = (inicio_nome + fim_sobrenome).lower()
    return usuario

nome_usuario = input("Digite o seu primeiro nome: ")
sobrenome_usuario = input("Digite o seu sobrenome: ")

nome_final = gerar_usuario(nome_usuario, sobrenome_usuario)
print(f"Seu nome de usuário gerado é: {nome_final}")