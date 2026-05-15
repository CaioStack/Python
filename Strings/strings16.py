# Crie uma função chamada `limpar_frase` que receba uma frase e retorne uma nova frase contendo apenas letras e espaços.

# Caracteres como números, pontos, vírgulas, exclamações e símbolos devem ser removidos.

def limpar_frase(frase):
    frase_limpa = ""
    
    for caractere in frase:
        # Verifica se o caractere é uma letra ou um espaço em branco
        if caractere.isalpha() or caractere.isspace():
            frase_limpa += caractere
            
    return frase_limpa

texto_sujo = "Olá, Mundo! 123... Python é 100% incrível."
texto_limpo = limpar_frase(texto_sujo)

print(f"Texto original: {texto_sujo}")
print(f"Texto limpo:    {texto_limpo}")