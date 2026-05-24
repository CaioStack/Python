# Crie uma função chamada mensagem_personalizada que recebe o
# nome de uma pessoa como argumento e retorna uma mensagem de
# saudação personalizada, como "Olá, [Nome]! Como você está?".
# Peça ao usuário para inserir seu nome e exiba a mensagem.

def mensagem_personalizada(nome):
    return f"Olá, {nome}! Como você está?"

nome_usuario = input("Digite seu nome: ")
mensagem = mensagem_personalizada(nome_usuario)
print(mensagem)