

""" Atributos de instancia:
self.pi  e  self.radius  são atributos de instancia
Pertencem a uma instância específica
Alterarndo os atributos de uma instância, isso não afetará outras instâncias.
Defini-se um atributo de instancia dentro do metodo __init__

class Circle:    
    def __init__(self, radius): # Metodo de inicalização
        self.pi = 3.14159 # Atributos de instância       
        self.radius = radius # Atributos de instância
        
    def area(self): # Metodo de instancia
        return self.pi * self.radius**2
        
    def circumference(self): # Metodo de instancia
        return 2*self.pi * self.radius
"""
"""  Introdução aos atributos de classe
O atributo de classe é definido fora dos metodos
"""

class Circle:

    pi = 3.14159 # Atributos de classe

    def __init__(self, radius):
        self.radius = radius # Atributos de instância
    def area(self):
        return self.pi * self.radius**2
    def circumference(self):
        return 2 * self.pi * self.radius

if __name__ == '__main__' :
    #from pprint import pprint

    bola_futsal = Circle(125)
    """ FORMAS DE ACESSO AO ATRIBUTO DE CLASSE """
    # FORMA 1: Atraves da instancia da classe
    print(bola_futsal.pi) # 3.14159
    # FORMA 2: Atraves da classe
    print(bola_futsal.pi) # 3.14159
