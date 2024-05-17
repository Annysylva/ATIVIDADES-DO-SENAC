def numeros_positivos(lista):
    positivos = []
    for numero in lista:
        if numero > 0:
            positivos.append(numero)
    return positivos

# Exemplo de uso:
lista_numeros = [-2, 5, -10, 8, 0, 3]
positivos_resultado = numeros_positivos(lista_numeros)
print(positivos_resultado)  # [5, 8, 3]
