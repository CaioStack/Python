lista_precos = [1500, 1000, 800, 2000]

def calcular_imposto(lista_valores):
    imposto_total = 0
    for valor in lista_valores:
        if valor > 1000:
            taxa = 0.15
        else:
            taxa = 0.1
        imposto = valor * taxa
        imposto_total += imposto
    return imposto_total

imposto_lista1 = calcular_imposto(lista_precos)
print(f"O imposto total para a lista de preços é: {imposto_lista1}")

lista_precos2 = [500, 4000, 3200, 2600, 1000]
imposto_lista2 = calcular_imposto(lista_precos2)
print(f"O imposto total para a segunda lista de preços é: {imposto_lista2}")