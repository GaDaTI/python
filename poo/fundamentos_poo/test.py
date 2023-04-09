"""
    class Cliente:

    def __init__(self, nome):
        self.nome = nome

    def get_nome(self):
        return print(self.nome)

    def set_nome(self, outro_nome):
        self.nome = outro_nome
        return self.nome

    pessoa = Cliente("Augus")
    print(pessoa.nome)
    pessoa.get_nome()
    pessoa.set_nome("Outro")
    pessoa.get_nome()

    """


class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def g_nome(self):
        return self.__nome


    @nome.setter
    def set_nome(self, outro_nome):
        self.__nome = outro_nome
        return self.__nome


if __name__ == '__main__':
    pessoa = Cliente("Augus")
    print(pessoa.g_nome)
    pessoa.nome("Outro")
    print(pessoa.g_nome)
