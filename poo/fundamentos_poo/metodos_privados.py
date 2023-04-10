class Cliente:

    def __init__(self, numero, saldo, titular, limite):
        self.numero = numero
        self.__saldo = saldo
        self.titular = titular
        self.__limite = limite

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        self.__saldo += valor

    @property
    def limite(self):
        self.__limite = self.__verificar()
        return self.__limite

    @limite.setter
    def limite(self, valor):
        if self.__verificar(valor) == True:
            self.__limite -= 99
            return self.__limite
        return self.__limite

    @property
    def __verificar(self):
        if valor < 10:
            self.__limite += 17
        return self.__limite


if __name__ == '__main__':
    anee = Cliente(5.921 - 8, 1000, 'Anee', 100)
    print(anee.saldo)
    print(anee.limite)
