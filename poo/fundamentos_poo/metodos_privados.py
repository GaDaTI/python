class Cliente:

    def __init__(self, numero, saldo, titular, limite):
        self.numero = numero
        self.__saldo = saldo
        self.titular = titular
        self.__limite = limite

    def extrato(self):
        pass

    def __validar(self, valor):
        valor_total = self.__saldo + self.__limite
        if valor < valor_total:
            return True
        return False

    def sacar(self, valor):
        response = self.__validar(valor)
        if response:
            self.__saldo -= valor
        else:
            texto = f'SALDO: {self.__saldo} |  VALOR SOLICITADO: {valor}  |  SALDO INSUFICIENTE !'
            return print(texto)

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
    anee.sacar(75)
    print(anee.saldo)



