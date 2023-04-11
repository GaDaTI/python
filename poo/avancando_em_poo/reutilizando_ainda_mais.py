class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    def dar_likes(self):
        self._likes += 1

    @property
    def likes(self):
        return self._likes

    @likes.setter
    def likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()


class Filme( Programa ):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao


class Series( Programa ):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas


if __name__ == '__main__':
    vingadores = Filme('vingadores - guerra infinita', 2018, 160)
    print(f'Nome: {vingadores.nome} - Ano: {vingadores.nome} - Horas: {vingadores.nome} - Ano: {vingadores.likes}')

    atlanta = Series('atlanta ', 2018, 2)
    print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas : {atlanta.temporadas} - Likes: {atlanta.likes}')
