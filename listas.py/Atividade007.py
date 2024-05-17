def nomes_iniciam_com_A(lista_nomes):
    return [nome for nome in lista_nomes if nome.startswith('A')]

# Exemplo de uso:
lista_nomes = ["Ana", "Arthur", "Bianca", "Carlos", "Alice"]
nomes_com_A = nomes_iniciam_com_A(lista_nomes)
print(nomes_com_A)  # ['Ana', 'Arthur', 'Alice']
