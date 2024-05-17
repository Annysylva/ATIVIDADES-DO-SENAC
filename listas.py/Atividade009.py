def nome_mais_longo(lista_nomes):
    return max((nome for nome in lista_nomes if len(nome) >= 6), key=len, default='')

# Exemplo de uso:
lista_nomes = ["Ana", "Arthur", "Bianca", "Carlos", "Alice"]
nome_longo = nome_mais_longo(lista_nomes)
print(f"O nome mais longo é: {nome_longo}")
