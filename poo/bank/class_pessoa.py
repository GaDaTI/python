from pprint import  pprint


class Pessoa:

    nacionalidade = 'brasileiro'

    def __init__(self, nome, sobrenome, idade, dd, mm, yyyy, estado_civil,  naturalidade ,  uf):
        """
        Dados de uma pessoa
        """
        self._nome = nome
        self._sobrenome = sobrenome
        self._idade = idade
        self._dia_de_nascimento = dd
        self._mes_de_nascimento = mm
        self._ano_de_nascimento = yyyy
        self._estado_civil = estado_civil
        self._naturalidade = naturalidade
        self._unidade_fiscal = uf




