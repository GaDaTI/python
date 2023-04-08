


class ContaCorrente:

    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite


if __name__ == '__main__' :
    """
    1. Instanciando o objeto
        conta_corrente_marques = ContaCorrente(8.765-4, 'Marques', 1.234, -1000)
    
    2. Atribuindo valores aos parametros  para a função de inicialização da classe.
    
    3. No momento em que chamamos a class  ContaCorrente passamos entre os parentêses valores (ARGUMENTOS) 
           que serão atribuidos para os parametros da função de inicialização def __init__(self, numero, titular, saldo, limite):
           
                  '  --------|   numero  |--------  ,--------|   titular  |--------  ,  --------|   saldo  |--------   ,   --------|   limite' |--------  '
    
    4. Assim o objeto  'conta_corrente_marques' terá os atributos de instância os valores atribuidos aos parametros:
                  
                    # self. numero = 8.765-4
                    # self. titular = Marques
                    # self. saldo = 1.234
                    # self. limite = -1000

    
    """
    conta_corrente_marques = ContaCorrente("8.765-4", 'Marques', "1.234", "-1000")
    for keys, value in conta_corrente_marques.__dict__.items():
        keys_str = "self." + f" {keys}"
        print(f"{keys_str} = {value}")









