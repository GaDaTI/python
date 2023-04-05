"""  INTROD UÇÃO AS PROPIEDADES DE CLASSE"""


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

"""  Para garantir a semantica correta  teriamos que fazer 
    toda vez :
    age = - 1
    if age <= 0:
        raise ValueError("BBMP")
    else:
        pessoa.age = age
     
       
    """


