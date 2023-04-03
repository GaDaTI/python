"""  Criando nossa 1ª Classe """

class TV:

    def __init__(self):
        self.tamanho = 20
        self.cor = 'Preta'
        self.canal = 'Netflix'
        self.volume = 10
        self.ligada =  False
    def mudar_canal(self, novo_canal):
        self.canal = novo_canal

    def mudar_volume(self):
        pass

    def ligar_desligar(self):
        pass

    def mostrar_canal(self):
        pass


tv_da_sala = TV()

print(tv_da_sala.canal) # Netflix
tv_da_sala.mudar_canal('Disney Plus')
print(tv_da_sala.canal)


