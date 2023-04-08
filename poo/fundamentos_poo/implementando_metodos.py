
class ContaCorrente:

    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def sacar(self, valor):
        self.saldo -= valor
        return self.saldo

    def limite(self, valor):
        pass

    def depositar(self, valor):
        pass

    def extrato(self):
        pass



if __name__ == '__main__' :
    conta_corrente_mauricio = ContaCorrente(3.452-1, 'Mauricio',  323.87,  100)

    print(conta_corrente_mauricio.limite)

    conta_corrente_mauricio.sacar(200)

    print(conta_corrente_mauricio.saldo)

    #for keys, values in conta_corrente_mauricio.__dict__.items():
    #    keys_str ='self.'+f'{keys}'
    #    print(f"{keys_str} = {values}")



