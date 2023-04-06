from class_pessoa import  Pessoa
from pprint import pprint

pablo = Pessoa('Pablo', 'Michigan', '47', '09', '11', '1976', 'Casado','Cururipe', 'AL')

if __name__ == '__main__' :
    pprint(pablo.__dict__)
    #pprint(Pessoa.__dict__)
