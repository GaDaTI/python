class Filme:
    def __init__(self, nome, ano, duracao):
        self.nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.likes = 0

    def dar_likes(self):
       self.likes += 1


class Series:
    def __init__(self, nome, ano, temporadas):
        self.nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.likes = 0

    def dar_likes(self):
        self.likes += 1


if __name__ == '__main__':
    vingadores = Filme('vingadores - guerra infinita', 2018, 160)
    print(f'Nome: {vingadores.nome} - Ano: {vingadores.nome} - Horas: {vingadores.nome} - Ano: {vingadores.likes}')


    atlanta = Series('atlanta ', 2018, 2)
    print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas : {atlanta.temporadas} - Likes: {atlanta.likes}')