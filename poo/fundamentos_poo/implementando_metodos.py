from datas import Data


class ContaCorrente:

    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def sacar(self, valor):

        if self.saldo > valor:
            self.saldo -= valor
        else:
            self.limite -= valor

        return valor

    def limite(self):
        return self.limite

    def depositar(self, valor):
        self.saldo += valor


    def extrato(self):
        texto = f"Titular: {self.titular}  |  Saldo em conta:  R$  {self.saldo}" | f"{data}"
        return texto


if __name__ == '__main__':




    #Instanciando um objeto
    conta_corrente_mauricio = ContaCorrente(3.452 - 1, 'Mauricio', 323.87, 100)

    # Acessando ao atributo de instancia diretamente
    print(conta_corrente_mauricio.limite)

    # Acessando ao metodo sacar() da classe ContaCorrente
    conta_corrente_mauricio.sacar(200)

    # Acessando ao metodo extrato() da classe ContaCorrente
    print(conta_corrente_mauricio.extrato())

    # for keys, values in conta_corrente_mauricio.__dict__.items():
    #    keys_str ='self.'+f'{keys}'
    #    print(f"{keys_str} = {values}")
