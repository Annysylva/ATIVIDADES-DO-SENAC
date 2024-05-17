numeros = input("Digite uma lista de numeros separados por virgula: ")
numeros = numeros.split(",")
maior = int(numeros[0])
for numero in numeros:
    if int(numero) > maior:
        maior = int(numero)
        print("O maior numero da listaé", maior)