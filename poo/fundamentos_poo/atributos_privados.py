"""  Atributos privados do Python """

""" Introdução ao encapsulamento em Python 
1. O encapsulamento é um dos quatro conceitos fundamentais na programação orientada a objetos, incluindo abstração, encapsulamento, herança 
e polimorfismo.
é o empacotamento de dados e funções que funcionam nesses dados em um único objeto.
"""
# Exemplo de encapsulamento Python

"""
class Counter:
    def __init__(self):
        self.current = 0

    def increment(self):
        self.current += 1

    def value(self):
        return self.current

if __name__ == '__main__' :
    relogio = Counter()
    print(relogio.value())
    relogio.increment()
    relogio.increment()
    relogio.increment()
    print(relogio.value())
    relogio.current = - 999
    print(relogio.value()) # - 999

"""

"""  Atributos privados  
Python não tem um conceito de atributos privados. Em outras palavras, todos os atributos são acessíveis de fora de uma classe.
Por convenção, você pode definir um atributo privado prefixando um único sublinhado (_):
_attribute

class Counter:
    def __init__(self):
        self._current = 0

    def increment(self):
        self._current += 1

    def value(self):
        return self.__current

if __name__ == '__main__' :
    relogio = Counter()
    print(relogio.value())
    relogio._current = - 999
    print(relogio.value())  # - 999
    

"""

"""  Alteração de nome com sublinhados duplos
 Se você prefixar um nome de atributo com sublinhados duplos ( __) assim:
 __attribute
 O Python mudará automaticamente o nome do __attribute para:
 _class__attribute
 
 """
class Counter:
    def __init__(self):
        self.__current = 0

    def increment(self):
        self.__current += 1

    def value(self):
        return self.__current

if __name__ == '__main__' :
    relogio = Counter()
    # Não poderá acessar o atributo diretamente de fora de uma classe
    # instance.__attribute
    #No entando ainda será possível acessar por meio do
    # instance.-Class__attribute
    print(relogio._Counter__current)



