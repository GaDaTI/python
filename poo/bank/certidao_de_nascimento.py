from class_pessoa import Pessoa
from pprint import pprint


class CertidaoDeNascimento(Pessoa):

    def __init__(self, sexo, dia, mes, ano, naturalidade, uf):
        self.sexo = sexo
        self._dia_de_nascimento = dia
        self._mes_de_nascimento = mes
        self._ano_de_nascimento = ano
        self._naturalidade = naturalidade
        self._unidade_fiscal = uf

# if __name__ == '__main__' :
