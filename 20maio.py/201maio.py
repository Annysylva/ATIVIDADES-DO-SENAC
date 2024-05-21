equipe1 = []
equipe2 = []
equipe3 = []
equipe4 = []
lista = 0
while lista < 10:
    nome = input(f'Entre com o nome para a equipe 1, ou "s" para sair: ')
    if nome == 's':
        break
    lista += 1
    equipe1.append(nome)
lista = 0
while lista < 10:
    nome = input(f'Entre com o nome para a equipe 2, ou "s" para sair: ')
    if nome == 's':
        break
    lista += 1
    equipe2.append(nome)
lista = 0
while lista < 10:
    nome = input(f'Entre com o nome para a equipe 3, ou "s" para sair: ')
    if nome == 's':
        break
    lista += 1
    equipe3.append(nome)
lista = 0
while lista < 10:
    nome = input(f'Entre com o nome para a equipe 4, ou "s" para sair: ')
    if nome == 's':
        break
    lista += 1
    equipe4.append(nome)
print("Equipe 1:", equipe1)
print("Equipe 2:", equipe2)
print("Equipe 3:", equipe3)
print("Equipe 4:", equipe4)

#Créditos: Jocilé