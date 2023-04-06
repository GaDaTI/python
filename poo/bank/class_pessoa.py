from pprint import  pprint


class Pessoa:

    nacionalidade = 'brasileiro'

    def __init__(self, nome, sobrenome, idade, dia_de_nascimento, mes_de_nascimento,
                 ano_de_nascimento, estado_civil,  na ,  uf):
        """
        Dados de uma pessoa
        """
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.dia_de_nascimento = dia_de_nascimento
        self.mes_de_nascimento = mes_de_nascimento
        self.ano_de_nascimento = ano_de_nascimento
        self.estado_civil = estado_civil
        self.naturalidade = na
        self.unidade_fiscal = uf

    def __str__(self):
        return f''' 
'''
if __name__ == '__main__' :
    pessoa = Pessoa()
    print(pessoa) # <__main__.Pessoa object at 0x7fab6f856a10>
    #pprint(pessoa.__dict__)
