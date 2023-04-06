from pprint import  pprint


class Pessoa:

    pais = {  'BR' : 'Brasil' }

    def __init__(self):
        """
        Dados de uma pessoa
        """
        self.nome = None
        self.sobrenome = None
        self.idade = None
        self.dia_de_nascimento = None
        self.mes_de_nascimento = None
        self.estado_civil = None
        self.cpf = None
        self.rg = None

    def dados_da_mae(self):
        pass





if __name__ == '__main__' :
    pessoa = Pessoa()
    print(pessoa) # <__main__.Pessoa object at 0x7fab6f856a10>
    #pprint(pessoa.__dict__)
    """
    {'cpf': None,
 'dia_de_nascimento': None,
 'estado_civil': None,
 'idade': None,
 'mes_de_nascimento': None,
 'nome': None,
 'rg': None,
 'sobrenome': None}
    """