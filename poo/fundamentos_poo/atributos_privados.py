"""  Atributos privados do Python

1. Conceitos fundaementais da programação orientada a objeto:

            1.1 - Encapsulamento
            1.2 -  Abstração
            1.3 -  Herança
            1.4 - Polimorfismo


1.1 - Encapsulamento :

        - > O encapsulamento em Python descreve o conceito de agrupar dados e metodos em uma unica unidade.

        - > Exemplo:  Uma classe

        - > Liga todos o membros de dados ( variaveis de instancia) e metodos  em uma unica unidade.


1.1.1 - Acesso as  atributos :

        1.1.1.a - Atributos Publicos:  Acessível em qualquer lugar fora da classe.


        1.1.1.b- Atributos Privados: Acessível dentro da classe


        1.1.1.c- Atributos Protegidos: Acessível dentro da classe e suas subclasses


"""


class Employee:

    # Metodo inicializador
    def __init__(self, name, salary):
        # Atributos privados de instancia
        self.__name = name
        self.__salary = salary

    # Metodo publico de instancia
    def show(self):
        return print("Name: ", self.__name, "Salary: ", self.__salary)


if __name__ == '__main__':
    # Instaciando um objeto
    funcionario = Employee('Jessica', 10000)

    # Tentativa de acesso dos atributos  privados de instancia da classe Employee
    # Retorna um AttributeError: 'Employee' object has no attribute '__name'
    #print("Name: ", funcionario.__name, "Salary: ", funcionario.__salary)


    # FORMAS DE ACESSO A ATRIBUTOS PRIVADOS

    # METODO 1 : NAME MANGLING
    # Trata-se de uma excessão para acessar atributos privados fora da classe NÃO RECOMENDADA !
    print("Name: ", funcionario._Employee__name, "Salary: ", funcionario._Employee__name)

    # METODO 2:  METODOS PUBLICOS PARA ACESSO ATRIBUTOS PRIVADOS
    # É a forma adotada por convenção
    funcionario.show() # Name:  Jessica Salary:  10000





