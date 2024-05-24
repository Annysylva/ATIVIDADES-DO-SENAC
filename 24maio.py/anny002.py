def contar_vogais_e_constantes(string):
    vogais = 'aeiouAEIOU'
    num_vogais = sum(1 for char in string if char in vogais)
    num_constantes = sum(1 for char in string if char.isalpha() and char not in vogais)
    return num_vogais, num_constantes
entrada = input("Digite uma string: ")
vogais, consoantes = contar_vogais_e_constantes(entrada)
print(f"vogais: {vogais}, consoantes: {consoantes}")
