from pessoa_brenda import brenda

class Correntista:

    def __init__(self):
        self.correntista = [ ]
        pass

    @property.setter
    def cadastro(self, pessoa ):
        """
        2-  Receber  os  9 dados do cliente  e  validar com uma menssagem de retorno
        """
        self.correntista.append(pessoa)
        pass

    @property.getter
    def correntista(self):
        print(f"Cadastro realizado")
        return self.cadastro

    def agencia(self):
        """
        3- Gerar o numero da agência com 4 algorismos no modelo 1111
        """
        pass

    def conta_corrente(self):
        """
        4- Gerar o numero da contacorrente  com 5 algarismos no modelo :  1.111-11
        """
        pass


if __name__ == '__main__' :
    cliente_brenda = Correntista.cadastro(brenda)
    print(cliente_brenda)