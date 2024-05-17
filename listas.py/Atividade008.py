def segundo_maior(lista):
    lista_ordenada = sorted(set(lista))
    return lista_ordenada[-2]

# Exemplo de uso:
lista_numeros = [10, 20, 4, 45, 99]
segundo_maior_resultado = segundo_maior(lista_numeros)
print(f"O segundo maior número é: {segundo_maior_resultado}")
