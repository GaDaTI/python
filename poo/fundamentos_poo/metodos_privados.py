class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome
        return self.__nome.upper()


if __name__ == '__main__':
    pessoa = Cliente('Vagner')
    print(pessoa.nome)
    pessoa.nome = 'Pedro'
    print(pessoa.nome)
