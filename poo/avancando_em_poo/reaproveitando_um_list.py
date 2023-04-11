class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.likes} likes'

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


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.duracao}  min - {self.likes} likes'


class Series(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.temporadas}  temporadas - {self.likes} likes'


class Playlist(list):

    def __init__(self, nome, programas):
        self.nome = nome
        super().__init__(programas)




if __name__ == '__main__' :
    vingadores = Filme('vingadores - guerra infinita', 2018, 160)
    atlanta = Series('atlanta ', 2018, 2)
    tmep = Filme('Todo mundo em panico', 1999, 100)
    demolidor = Series('Demolidor', 2016, 2)

    atlanta.dar_likes()
    tmep.dar_likes()
    tmep.dar_likes()
    tmep.dar_likes()
    demolidor.dar_likes()
    demolidor.dar_likes()
    demolidor.dar_likes()
    demolidor.dar_likes()
    atlanta.dar_likes()
    atlanta.dar_likes()
    vingadores.dar_likes()

    filmes_e_series = [vingadores, atlanta, demolidor, tmep]
    playlist_fim_de_semana = Playlist('Fim de semana', filmes_e_series)

    print(f'Tamanho da Playlis : {len(playlist_fim_de_semana)}')

    print(f'Demolidor está ou não dentro da playlist fim de semana : {demolidor in playlist_fim_de_semana}')

    for item in playlist_fim_de_semana:
        print(item)