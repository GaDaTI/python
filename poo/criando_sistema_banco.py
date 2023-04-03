""" Criando um Sistema de Conta Corrente"""

from datetime import datetime
import pytz

class ContaCorrente:

    def __init__(self, nome, cpf, numero_ag, numero_cc):
        self._nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None
        self.agencia = numero_ag
        self.conta = numero_cc
        self.transacoes = [ ]
    def consultar_saldo(self):
        texto = 'O seu saldo atual é de {}'.format(self.saldo)
        return texto

    def _limite_conta(self):
        self.limite = -1000
        return self.limite
    def sacar(self, valor):
        if self.saldo - valor < self._limite_conta():
            print("Você não possui saldo suficiente !")
            self.consultar_saldo()
        else:
            self.saldo -= valor
            self.transacoes.append((valor, self.saldo, ContaCorrente._data_hora()))
        pass
    def depositar(self, valor):
        self.saldo += valor
        self.transacoes.append((valor, self.saldo, ContaCorrente._data_hora()))
        pass
    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y  %H:%H:%S')
    def consultar_historico_transacoes(self, transacoes):
        print('Historico de transações')
        for transacoes in self.transacoes:
            print(transacoes)



if __name__ == '__main__':
    # cliente = ContaCorrente()
    # print(cliente.nome) # None
    # print(cliente.cpf) # None
    cliente_gabriel = ContaCorrente('Gabriel', '453.923.225-49', '1510', '1731-6')
    print(cliente_gabriel .consultar_saldo())
    cliente_gabriel .depositar(343)
    print(cliente_gabriel .consultar_saldo())
    cliente_gabriel .sacar(934)    # print(cliente.consultar_saldo())
    cliente_gabriel .consultar_historico_transacoes(50)
    cliente_afonso = ContaCorrente( 'Afonso', '711.961.805-23', '1510', '2242-8')
    print(cliente_afonso.consultar_saldo())
    print(cliente_afonso.nome)
    print(cliente_afonso.agencia)

    # print(cliente.nome) # Gabriel
    # print(cliente.cpf) # 453.923.225-49
