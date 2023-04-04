"""
Objetos:  é um contêiner que contém dados e funcionalidades .
Os dados representam o objeto em um determinado momento no tempo.
Portanto, os dados de um objeto são chamados de estado .
 Python usa atributos para modelar o estado de um objeto.
"""

# Palavra chave : class  |  Nome da class: Person

class Person:
    pass

# Para cirar uma instancia de uma classe

person = Person( )

print(person) # Nome e endereço de memória  : <__main__.Person object at 0x7f9175c16ad0>

# Para obter a identidade de um objeto

print(id(person)) # 140604991695568

# Para obter a identidade de um objeto

print(hex(id(person))) # 0x7f4eb9016ad0

# A isinstance()f unção retorna Truese um objeto é uma instância de uma classe

print(isinstance(person, Person)) # True

# Quando você define a Personclasse, o Python cria um objeto com o nome Person. O Personobjeto tem atributos. Por exemplo,
# você pode encontrar seu nome usando o __name__atributo:
print(Person.__name__) # Person

# O Personobjeto tem o tipo de type:
print(type(Person)) # <class 'type'>

# A Personclasse também tem um comportamento. Por exemplo, ele pode criar uma nova instância:
person = Person ( )
print(type(person)) # <class '__main__.Person'>