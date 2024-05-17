def numero_mais_frequente(lista):
    return max(set(lista), key=lista.count)

# Exemplo de uso:
lista_numeros = [2, 1, 2, 2, 1, 3]
numero_frequente = numero_mais_frequente(lista_numeros)
print(f"O número mais frequente é: {numero_frequente}")
