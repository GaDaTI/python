from  class_pessoa import  Pessoa
from pprint import pprint

if __name__ == '__main__' :
    marcos = Pessoa( )
    print(marcos) # <class_pessoa.Pessoa object at 0x7fda0171aa10>
    pprint( marcos.__dict__)
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
    print(marcos.__doc__)