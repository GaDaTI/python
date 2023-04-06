from pprint import  pprint


class Pessoa:

    pais = {  'BR' : 'Brasil' }

    def __init__(self, nome, sobrenome, idade, dia_de_nascimento, mes_de_nascimento, ano_de_nascimento, estado_civil, cpf, rg):
        """
        Dados de uma pessoa
        """
        self.__nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.dia_de_nascimento = dia_de_nascimento
        self.mes_de_nascimento = mes_de_nascimento
        self.ano_de_nascimento = ano_de_nascimento
        self.estado_civil = estado_civil
        self.cpf = cpf
        self.rg = rg
        print(f"Construindo o objeto ... {self}")

    def __str__(self):
    nome = nome
    sobrenome = sobrenome
    idade = idade
    dia_de_nascimento = dia_de_nascimento
    mes_de_nascimento = mes_de_nascimento
    ano_de_nascimento = ano_de_nascimento
    estado_civil = estado_civil
    cpf = cpf
    rg = rg 





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