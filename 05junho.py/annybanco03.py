class ContaAnnySylva:
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


class SistemaBancario:
    def __init__(self):
        self.conta = None

    def iniciar_sistema(self):
        nome_usuario = input("Digite o nome do usuário: ")
        self.conta = ContaAnnySylva(nome_usuario)

        while True:
            print("\nOpções:")
            print("1. Depositar")
            print("2. Sacar")
            print("3. Extrato")
            print("4. Sair")
            opcao = int(input("Escolha uma opção: "))

            if opcao == 1:
                valor_deposito = float(input("Digite o valor do depósito: "))
                self.conta.depositar(valor_deposito)
            elif opcao == 2:
                valor_saque = float(input("Digite o valor do saque: "))
                self.conta.sacar(valor_saque)
            elif opcao == 3:
                self.conta.extrato()
            elif opcao == 4:
                print("Saindo do sistema.")
                break
            else:
                print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    sistema = SistemaBancario()
    sistema.iniciar_sistema()