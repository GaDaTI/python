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


1.1.1 - Acesso aos  atributos  privados ou protegidos :

         A convensão para acesso aos atributos privados ou protegidos no Python é por meio de metodos.

         Essses Metodos recebem os seguintes nomes:

                        Método getter  :
                        Utilizados para acessar os atributos privados ou protegidos.

                        Métodos setter  :
                        Utilizados para modificar os atributos privados ou protegidos .

"""



class Employee:

    # Metodo inicializador
    def __init__(self, name, salary):
        # Atributos publicos
        self.__name = name
        self._salary = salary

    # Metodo setter para acessar  e modificar um atributo privado
    def name_change(self, outro_nome):
        self.__name = outro_nome
        return self.__name

    # Metodo getter para acessar  e modificar  um atributo protegido
    def salary_change(self, fator):
        self._salary *= fator
        return self._salary

    # Metodo getter para acessar e retornar um atributo privado
    def name_show(self):
        return self.__name

    # Metodo getter para acessar e retornar um atributo protegido
    def salary_show(self):
           return self._salary




if __name__ == '__main__':
    # Instaciando um objeto
    funcionario = Employee('Jessica', 10000)

    # Metodo getter para acessar e retornar o valor do atributo privado name
    print(funcionario.name_show())

    # Metodo getter para acessar e retornar o valor do atributo privado salary
    print(funcionario.salary_show())

    # Metodo setter para acessar  e modificar o valor do atributo privado name
    funcionario.name_change('Wagshinton')

    # Metodo getter para acessar  e modificar  o valor do atributo privado salary
    funcionario.salary_change(1.1)

    # Metodo getter para acessar e retornar o valor do atributo privado name
    print("O nome modifcado usando setter: " , funcionario.name_show())

    # Metodo getter para acessar e retornar o valor do atributo privado salary
    print("O salario modifcado usando setter: " , funcionario.salary_show())



