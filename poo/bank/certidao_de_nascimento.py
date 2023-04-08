from class_pessoa import Pessoa
from endereco import Endereco
from pprint import pprint


class CertidaoDeNascimento(Pessoa, Endereco):

    def __init__(self, sexo, dia, mes, ano, naturalidade, uf, _nome,_sobrenome):
        super().__init__(_nome, _sobrenome)
        self.sexo = sexo
        self._dia_de_nascimento = dia
        self._mes_de_nascimento = mes
        self._ano_de_nascimento = ano
        self._naturalidade = naturalidade
        self._unidade_fiscal = uf

    def endereco_nascimento(cls, rua, bairro, nome, cidade, estado):
       pass

# if __name__ == '__main__' :
