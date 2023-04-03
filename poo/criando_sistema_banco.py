""" Criando um Sistema de Conta Corrente"""


class ContaCorrente:

    def __init__(self, nome=None, cpf=None):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
    def consultar_saldo(self):
        texto = 'O seu saldo atual é de {}'.format(self.saldo)
        return texto

    def sacar(self, valor):
        if self.saldo - valor < 0:
            print("Você não possui saldo suficiente !")
            self.consultar_saldo()
        else:
            self.saldo -= valor
        pass
    def depositar(self, valor):
        self.saldo += valor
        pass


if __name__ == '__main__':
    # cliente = ContaCorrente()
    # print(cliente.nome) # None
    # print(cliente.cpf) # None
    cliente = ContaCorrente('Gabriel', '453.923.225-49')
    print(cliente.consultar_saldo())
    cliente.depositar(50_000)
    print(cliente.consultar_saldo())
    cliente.sacar(12345)
    print(cliente.consultar_saldo())
    # print(cliente.nome) # Gabriel
    # print(cliente.cpf) # 453.923.225-49


