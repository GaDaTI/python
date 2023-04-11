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
    vingadores.dar_likes()
    print(f'{vingadores.nome} - {vingadores.duracao} -  {vingadores.likes} ')
    atlanta = Series('atlanta ', 2018, 2)
    atlanta.dar_likes()
    atlanta.dar_likes()
    print(f'{atlanta.nome} -  {atlanta.ano} -  {atlanta.temporadas} ')

    filmes_e_series = [vingadores, atlanta]

    for item in filmes_e_series:
        detalhes = item.duracao if hasattr(item, 'duracao') else item.temporadas
        print(f'{item.nome}   - {detalhes}  D -  {item.likes} ')