vogais = 'aeiou'
soma_consoantes = 0
soma_vogais = 0
texto = input("Digite uma string: ").lower()

for letra in texto:
    if letra in vogais:
        soma_vogais +=1
    elif letra.isalpha():
        soma_consoantes +=1
        print(f"vogais: {soma_vogais}")
        print(f"consoantes: {soma_consoantes}")
