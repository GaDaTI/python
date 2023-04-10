class Cliente:

    def __init__(self, numero, saldo, titular, limite):
        self.numero = numero
        self.__saldo = saldo
        self.titular = titular
        self.__limite = limite


    @property
    def __verificar(self):
        if self.__limite < 10:
            return True

    def sacar(self, valor):
        self.__saldo -= valor

    def depositar(self, valor):
        self.__saldo -= valor

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite







if __name__ == '__main__':
    anee = Cliente(5.921 - 8, 1000, 'Anee', 100)
    print(anee.saldo)
    print(anee.limite)
