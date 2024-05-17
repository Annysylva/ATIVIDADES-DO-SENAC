def numeros_pares(lista):
    pares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
    return pares

# Exemplo de uso:
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8]
pares_resultado = numeros_pares(lista_numeros)
print(pares_resultado)  # [2, 4, 6, 8]
