
class ContaCorrente:

    def __init__(self, numero, titular,  saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite


if __name__ == '__main__':

    """
    1. Para acessar os atributos de instancia fora daclasse de maneira direta é necessario declarar:
    
                          |--->  nome_do_objeto   <---|  |--->  ponto  <---|  |--->  nome_do_atributo   <---|
                               conta_corrente_mario                      .                                 saldo
    
    """
    conta_corrente_mario = ContaCorrente('2.345-9', 'Mario', '438.9', -100)
    print(conta_corrente_mario.saldo) # 438.9









