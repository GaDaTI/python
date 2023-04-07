from class_pessoa import Pessoa
from certidao_de_nascimento import CertidaoDeNascimento
from pprint import pprint


class PessoaBrenda(Pessoa, CertidaoDeNascimento):
    def __init__(self, _nome, _sobrenome, sexo, dia, mes, ano, estado_civil, naturalidade, uf ):
        super().__init__( _nome, _sobrenome, sexo, dia, mes, ano, estado_civil, naturalidade, uf )
        super().__init__()






if __name__ == '__main__' :
     brenda = PessoaBrenda('Brenda', 'Waylle')
     pprint(brenda.__dict__)





