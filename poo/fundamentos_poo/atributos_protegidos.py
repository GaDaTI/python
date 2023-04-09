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
        # Atributos publicos
        self._name = name
        self._salary = salary

    # Metodo publico de instancia
    def show(self):
        print("Name: ", self._name, "Salary: ", self._salary)


if __name__ == '__main__':
    # Instaciando um objeto
    funcionario = Employee('Jessica', 10000)

    # Acessando atributos de instancia da classe Employee
    print("Name: ", funcionario._name, "Salary: ", funcionario._salary)
