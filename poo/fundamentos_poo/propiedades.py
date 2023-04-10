

class Cliente:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome.title()

    @nome.setter
    def nome(self, valor):
        self.__nome = valor


if __name__ == '__main__':
    pessoa = Cliente( 'Um')
    print(pessoa.nome)
    pessoa.nome = "Augus"
    print(pessoa.nome)
    pessoa.nome = "depende"
    print(pessoa.nome)
