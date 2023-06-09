"""  INTROD UÇÃO AS PROPIEDADES DE CLASSE


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == '__main__' :
    # Atribuições sematicamente corretas
    pessoa = Person('John', 23)
    print(f"pessoa.age: {pessoa.age}, pessoa.name: {pessoa.name}")

    # Atribuindo um valor semanticamente incorreto
    pessoa.age = - 14
    print(f"pessoa.age: {pessoa.age}, pessoa.name: {pessoa.name}")


Para garantir a semantica correta  teriamos que fazer
    toda vez :
    age = - 1
    if age <= 0:
        raise ValueError("BBMP")
    else:
        pessoa.age = age

"""



"""  GETTER  E SETTER 
# O getter retorna o valor de um atributo
# O setter define um novo valor para um atributo

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.set_age(age)
# 
#     def set_age(self ,  age):
#         if age <= 0:
#             raise ValueError('The age must be positive')
#         self._age = age
# 
#     def get_age(self):
#         return self._age
# 
# 
# if __name__ == '__main__' :
#     pessoa = Person('Mugni', 25)
#     print(pessoa.name)
#     print(pessoa.get_age())
#     #pessoa.set_age(-78)
#     #print(pessoa.get_age())
#     for metodo in dir(property()):
#         print(metodo)
 """

"""  A CLASSE DE PROPIEDADE """



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_age(self,  age):
        if age <= 0:
            raise ValueError("The value must be positive")
        self._age = age

    def get_age(self):
        return  self._age

    age = property(fget=get_age, fset=set_age)



if __name__ == '__main__' :
    from pprint import  pprint
    """  OBJETO DE PROPIEDADE : """
    #print(Person.age) # <property object at 0x7f5d0b71f1a0>


    pessoa = Person('Bau', 23)
    pprint(pessoa.__dict__) # {'name': 'Bau', '_age': 23}

    pessoa.age = 19
    pprint(Person.__dict__)






