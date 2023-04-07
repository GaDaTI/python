from class_pessoa import Pessoa
from certidao_de_nascimento import CertidaoDeNascimento
from pprint import pprint


class PessoaBrenda(Pessoa, CertidaoDeNascimento):
    def __init__(self, nome):
        super()._nome = nome




if __name__ == '__main__' :
     brenda = PessoaBrenda()




