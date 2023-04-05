

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
"""
class Circle:
    circle_list = [ ]
    pi = 3.14159 # Atributos de classe

    def __init__(self, radius):
        self.radius = radius # Atributos de instância
        self.circle_list.append(self)

    def area(self):
        return self.pi * self.radius**2

    def circumference(self):
        return 2 * self.pi * self.radius


if __name__ == '__main__' :
    #from pprint import pprint

    bola_futsal = Circle(125)
    #FORMAS DE ACESSO AO ATRIBUTO DE CLASSE 
    # FORMA 1: Atraves da instancia da classe
    print(bola_futsal.pi) # 3.14159
    # FORMA 2: Atraves da classe
    print(bola_futsal.pi) # 3.14159

     #QUANDO USAR OS ATRIBUTOS DE CLASSE PYTHON 
    # CASO 1/3 - Armazenamento constantes de classe
    # Uma constancia que não muda de uma instancia para instancia
    bola_de_campo = Circle(123)
    print(f"Bola de  campo, valor do atributo de classe  : {bola_de_campo.pi}")
    bola_de_volei = Circle(89)
    print(f"Bola de volei, valor do atributo de classe  : {bola_de_volei.pi}")

    # CASO 2/3 - Rastreamento de dados em todas as instâncias
    bola_tenis = Circle(10)
    bola_golf = Circle(5)
    print(len(Circle.circle_list))
"""
#FORMAS DE ACESSO AO ATRIBUTO DE CLASSE
# CASO 3/3 - Definição de valores padrão

class Product:

    default_discount = 0

    def __init__(self, price):
        self.price = price
        self.discount = Product.default_discount

    def set_discount(self, discount):
        self.discount = discount

    def net_price(self):
        return self.price * (1 - self.discount)


if __name__ == '__main__' :
    # Testando produto 1
    product_short = Product(100)
    product_short.set_discount(0.05)
    print(product_short.net_price()) # 95.0

    # Testando produto 2
    product_jacket = Product(200)
    product_jacket.set_discount(0.05)
    print(product_jacket.net_price()) # 190.0

