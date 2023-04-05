""" INTRODUÇÃO AOS METODOS DE CLASSE DO PYTHON """


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def introduce(self):
        return f"Hi. I'm {self.first_name} {self.last_name}. I'm {self.age} years old."

    @classmethod
    def create_anonymous(cls):
        return Person('John', 'Doe',  25)

if __name__ == '__main__' :
    jogador = Person('Carlos', 'Santana', 45)
    print(jogador.introduce())

    """ CHAMANDO METODOS DE CLASSE DO PYTHON """
    # ClassName.method_name()
    # método de fábrica
    anonymous = Person.create_anonymous()
    print(anonymous.introduce())

