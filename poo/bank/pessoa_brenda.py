from class_pessoa import Pessoa
from class_cliente import *


brenda = Pessoa( 'Brenda', 'Albuquerque',  '23',  '14',  '02' ,  '1983',  'solteira', 'Salvador', 'BA')


if __name__ == '__main__' :
    for keys, value in brenda.__dict__.items():
        print(value)



