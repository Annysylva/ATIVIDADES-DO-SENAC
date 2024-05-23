# Criar 3 operações bancárias: depósito, saque e extrato.

# Menu pra escolher
menu = '''
Escolha:
  [d] depósitar
  [s] sacar
  [e] extrato
  [x] sair
'''
saldo = 0
limite_de_saque = 500
quantidade_de_saques = 3
while True:
    opcao = input(menu)
    if opcao == 'x': break
    # Depósito
    if opcao == 'd':
        valor = float(input('Digite o valor do depósito: R$ '))
        if valor > 0 :
            saldo += valor  # equivale a saldo + valor
            print(f'Depósito de R$ {valor} confirmado!\nSaldo: R$ {saldo}')
    # Saque
    if opcao == 's':
        valor = float(input('Digite o valor do saque: R$ '))
        if quantidade_de_saques > 0:
            if valor <= saldo:
                saldo -= valor
                print(f'Saque de R$ {valor} confirmado!\nSaldo: R$ {saldo}')
            else:
                print(f'Infelizmente não será possível sacar o dinheiro por falta de saldo\nSaldo: R$ {saldo}')
        else:
            print(f'Infelizmente não será possível sacar o dinheiro por limite de saques')

# Extrato