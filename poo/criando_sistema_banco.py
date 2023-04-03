""" Criando um Sistema de Conta Corrente"""

class ContaCorrente:

    def __init__(self, nome=None, cpf=None):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None
    def consultar_saldo(self):
        texto = 'O seu saldo atual é de {}'.format(self.saldo)
        return texto
    def limite_conta(self):
        self.limite =  -1000
        return self.limite
    def sacar(self, valor):
        if self.saldo - valor < self.limite_conta( ):
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
    cliente.depositar(343)
    print(cliente.consultar_saldo())
    cliente.sacar(934)
    print(cliente.consultar_saldo())
   print(cliente.limite_conta)
    # print(cliente.nome) # Gabriel
    # print(cliente.cpf) # 453.923.225-49


