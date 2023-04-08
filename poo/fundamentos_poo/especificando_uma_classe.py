

class Sistema:
    def __init__(self):
        self.texto = None

    def le_entrada(self):
        self.texto = input()

    def exibe_saida(self):
        return self.texto


if __name__ == '__main__' :
    sistema = Sistema( )
    sistema.le_entrada()
    print(sistema.exibe_saida())




















