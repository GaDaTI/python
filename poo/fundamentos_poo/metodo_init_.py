"""    Introdução ao método Python __init__()    """


# Quando se cria uma classe , o Python chama automaticamente o __init__ para inicializar os atributos do objeto
# Metodos com dunder não são usados explicitamente

#class Person:
#   def __init__(self, name, age):
#       self.name = name
#       self.age = age

# def __init__(self, name, age): Quando o init possui parametros diferentes do self é necessario argumento na inicialização do objeto.

#if __name__ == '__main__' :
 #   person = Person('Jhon', 25)
 #   print(f"I'm {person.name}. I'm {person.age} years old.")


"""  O método __init__ com parâmetros padrão  """

class PersonOld:
    def __init__(self,  age, name='Merci'):
        self.name = name
        self.age = age


if __name__ == '__main__' :
    person_old = PersonOld(25)
    # I'm Merci. I'm 25 years old.
    print(f"I'm {person_old.name}. I'm {person_old.age} years old.")