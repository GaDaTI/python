from pprint import  pprint


class Pessoa:

    nacionalidade = 'brasileiro'

    def __init__(self, nome, sobrenome, idade, dd, mm, yyyy, estado_civil,  naturalidade ,  uf):
        """
        Dados de uma pessoa
        """
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.dia_de_nascimento = dd
        self.mes_de_nascimento = mm
        self.ano_de_nascimento = yyyy
        self.estado_civil = estado_civil
        self.naturalidade = naturalidade
        self.unidade_fiscal = uf




