class Cliente:

    def __init__(self, numero, saldo, titular, limite):
        self.numero = numero
        self.saldo = saldo
        self.titular = titular
        self.limite = limite

        





if __name__ == '__main__':
    conta_tr = Cliente(1221)
    print(conta_tr.saldo)
    conta_tr.saldo = -20000

