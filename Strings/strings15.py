# Uma loja usa códigos de produto com as seguintes regras:

# - Deve ter exatamente 6 caracteres
# - Os 2 primeiros caracteres devem ser letras
# - Os 4 últimos caracteres devem ser números

# Crie uma função chamada `validar_codigo` que receba um código e retorne se ele é válido ou inválido.

def validar_codigo(codigo):
    """Valida se o código possui 6 caracteres (2 letras iniciais e 4 números finais)."""
    if len(codigo) != 6:
        return "Inválido"

    letras = codigo[:2]
    numeros = codigo[2:]
    
    if letras.isalpha() and numeros.isdigit():
        return "Válido"
    else:
        return "Inválido"

print(f"Código AA1234: {validar_codigo('AA1234')}")  # Retorna Válido
print(f"Código A12345: {validar_codigo('A12345')}")  # Retorna Inválido (apenas 1 letra)
print(f"Código ABC123: {validar_codigo('ABC123')}")  # Retorna Inválido (3 letras)
print(f"Código AA123:  {validar_codigo('AA123')}")   # Retorna Inválido (curto demais)