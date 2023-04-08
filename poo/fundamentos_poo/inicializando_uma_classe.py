class ContaCorrente:

    def __init__(self, numero, titular, saldo, limite):
        """
        Atributos de uma instancia estão colocados  dentro do scopo do __init__ . São carcteristicas de uma classe:
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        """
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        pass


if __name__ == '__main__':
    conta_corrent_wadson = ContaCorrente(4832 - 8, 'Wadson', 123.0, 0)
    for keys, values in conta_corrent_wadson.__dict__.items():
        print(values)
