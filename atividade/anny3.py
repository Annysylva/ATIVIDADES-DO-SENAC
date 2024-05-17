frase = input("Digite uma frase: ")
vogais = "aeiou"
contagem = 0
for letra in frase:
    if letra.lower() in vogais:
        contagem += 1
        print("Afrase digitada possui", contagem, "vogais.")