from class_pessoa import Pessoa
from certidao_de_nascimento import CertidaoDeNascimento
from pprint import pprint


class PessoaBrenda(Pessoa):
    def __init__(self, nome, sobrenome, estado_civil):
        super().__init__( nome, sobrenome, estado_civil )






if __name__ == '__main__' :
     brenda = PessoaBrenda('Brenda', 'Waylle', 'Casada')
     pprint(brenda.__dict__)





