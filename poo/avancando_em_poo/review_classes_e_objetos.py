class Filme:
    def __init__(self, nome, ano, duracao):
        self.nome = nome
        self.ano = ano
        self.duracao = duracao

class Series:
    def __init__(self, nome, ano, temporadas):
        self.nome = nome
        self.ano = ano
        self.temporadas = temporadas


if __name__ == '__main__':
    vingadores = Filme('Vingadores - Guerra Infinita', 2018, 160)
    print(f'Nome: {vingadores.nome} - Ano: {vingadores.nome} - Horas: {vingadores.nome}')


    atlanta = Series('Atlanta ', 2018, 160)
    print(f'Nome: {atlanta.nome} - Ano: {atlanta.nome} - Horas: {atlanta.nome}')


    """
    class Filme:
        pass
    
    
    if __name__ == '__main__':
        vingadores = Filme()
        #<__main__.Filme object at 0x7f7408c16ad0>
        print(vingadores)
        
    """
