# Crie um programa que peça ao usuário para digitar uma senha. Depois, crie uma função chamada `validar_senha` que receba essa senha e retorne `True` se ela for válida ou `False` se for inválida.

# A senha será considerada válida somente se atender a todas as regras abaixo:

# - Ter pelo menos 8 caracteres
# - Não possuir espaços
# - Possuir pelo menos uma letra maiúscula
# - Possuir pelo menos uma letra minúscula
# - Possuir pelo menos um número

def validar_senha(senha):
    if len(senha) < 8:
        return False
        
    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False
    
    for caractere in senha:
        if caractere.isspace():
            return False
            
        if caractere.isupper():
            tem_maiuscula = True
            
        elif caractere.islower():
            tem_minuscula = True

        elif caractere.isdigit():
            tem_numero = True
            
    return tem_maiuscula and tem_minuscula and tem_numero

senha_usuario = input("Digite a senha para validação: ")

if validar_senha(senha_usuario):
    print("Senha Válida!")
else:
    print("Senha Inválida!")