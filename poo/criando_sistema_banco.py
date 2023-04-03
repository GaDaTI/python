""" Criando um Sistema de Conta Corrente"""

class ContaCorrente:

    def __init__(self, nome=None, cpf=None):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0

    def consultar_saldo(self):
        texto = 'O seu saldo atual é de {}'.format(self.saldo)
        return texto

if __name__ == '__main__':
    cliente = ContaCorrente()
    print(cliente.nome) # None
    print(cliente.cpf) # None
    cliente = ContaCorrente('Gabriel', '453.923.225-49')
    print(cliente.nome) # Gabriel
    print(cliente.cpf) # 453.923.225-49
    print(cliente.consultar_saldo())
