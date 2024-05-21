class ContaBancaria:
    def __init__(self, nome):
        self.nome = nome
        self.saldo = 0
        self.depositos = []
        self.saques = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f"Depósito de R$ {valor:.2f} realizado. Saldo atual: R$ {self.saldo:.2f}")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if valor > 0 and valor <= 500:
            if self.saldo >= valor:
                self.saldo -= valor
                self.saques.append(valor)
                print(f"Saque de R$ {valor:.2f} realizado. Saldo atual: R$ {self.saldo:.2f}")
            else:
                print("Saldo insuficiente para saque.")
        else:
            print("Valor inválido para saque.")

    def extrato(self):
        print("\nExtrato:")
        for deposito in self.depositos:
            print(f"Depósito: R$ {deposito:.2f}")
        for saque in self.saques:
            print(f"Saque: R$ {saque:.2f}")
        print(f"Saldo atual: R$ {self.saldo:.2f}")

# Exemplo de uso
if __name__ == "__main__":
    nome_usuario = input("Digite o nome do usuário: ")
    conta = ContaBancaria(nome_usuario)

    while True:
        print("\nOpções:")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Extrato")
        print("4. Sair")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            valor_deposito = float(input("Digite o valor do depósito: "))
            conta.depositar(valor_deposito)
        elif opcao == 2:
            valor_saque = float(input("Digite o valor do saque: "))
            conta.sacar(valor_saque)
        elif opcao == 3:
            conta.extrato()
        elif opcao == 4:
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")
