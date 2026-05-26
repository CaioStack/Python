# Crie um programa que simule um pequeno cadastro de usuário.

# O programa deve pedir:

# - Nome
# - E-mail
# - Senha

# Depois, crie funções para validar cada informação:

# - `validar_nome(nome)`
#     - O nome deve ter pelo menos 3 caracteres
#     - O nome deve conter apenas letras e espaços
# - `validar_email(email)`
#     - O e-mail deve conter `@`
#     - O e-mail deve conter `.`
#     - O e-mail não pode conter espaços
# - `validar_senha(senha)`
#     - A senha deve ter pelo menos 8 caracteres
#     - Deve possuir pelo menos uma letra e pelo menos um número

# Ao final, o programa deve informar se o cadastro foi aceito ou recusado.

def validar_nome(nome):
    if len(nome) < 3:
        return False
    if not all(c.isalpha() or c.isspace() for c in nome):
        return False
    return True

def validar_email(email):
    if '@' not in email or '.' not in email:
        return False
    if ' ' in email:
        return False
    return True

def validar_senha(senha):
    if len(senha) < 8:
        return False
    if not any(c.isalpha() for c in senha):
        return False
    if not any(c.isdigit() for c in senha):
        return False
    return True

def main():
    nome = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")

    if validar_nome(nome) and validar_email(email) and validar_senha(senha):
        print("Cadastro aceito!")
    else:
        print("Cadastro recusado!")
if __name__ == "__main__":
    main()