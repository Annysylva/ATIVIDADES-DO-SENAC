class ContaBancaria:
    def __init__(self):
        self.saldo = 0
        self.limite_de_saque = 500
        self.quantidade_de_saques = 3

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R$ {valor} confirmado!\nSaldo: R$ {self.saldo}')
        else:
            print('Valor inválido para depósito.')

    def sacar(self, valor):
        if self.quantidade_de_saques > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                self.quantidade_de_saques -= 1
                print(f'Saque de R$ {valor} confirmado!\nSaldo: R$ {self.saldo}')
            else:
                print(f'Saldo insuficiente para saque de R$ {valor}.')
        else:
            print('Limite de saques atingido.')

    def extrato(self):
        print(f'Saldo atual: R$ {self.saldo}')

if __name__ == '__main__':
    conta = ContaBancaria()
    while True:
        print('\nEscolha uma opção:')
        print('[d] Depósito')
        print('[s] Saque')
        print('[e] Extrato')
        print('[x] Sair')
        opcao = input('Digite a opção desejada: ')
        if opcao == 'x':
            break
        elif opcao == 'd':
            valor = float(input('Digite o valor do depósito: R$ '))
            conta.depositar(valor)
        elif opcao == 's':
            valor = float(input('Digite o valor do saque: R$ '))
            conta.sacar(valor)
        elif opcao == 'e':
            conta.extrato()
        else:
            print('Opção inválida. Tente novamente.')
