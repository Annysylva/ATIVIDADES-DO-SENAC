'''
Faça um algoritmo para cadastrar os alunos que estão se canditando para equipes de desenvolvimento
'''

equipe1 = []
equipe2 = []
equipe3 = []
equipe4 = []

lista = 0
while lista<10:
  nome = (input('Entre com o nome para a equipe 1, ou s pra sair: '))
  if nome == 's': break
  lista = lista + 1
  equipe1.append(nome)

while lista<10:
  nome = (input('Entre com o nome para a equipe 2, ou s pra sair: '))
  if nome == 's': break
  lista = lista + 1
  equipe2.append(nome)

while lista<10:
  nome = (input('Entre com o nome para a equipe 3, ou s pra sair: '))
  if nome == 's': break
  lista = lista + 1
  equipe3.append(nome)

while lista<10:
  nome = (input('Entre com o nome para a equipe 4, ou s pra sair: '))
  if nome == 's': break
  lista = lista + 1
  equipe4.append(nome)

# Desafio:
# Mostre os nomes por cada equipe
# Mostre os nomes que se repetem em outras equipes