"""  Criando nossa 1ª Classe """

class TV:

    def __init__(self,  canal, estado):
        self.tamanho = 20
        self.cor = 'Preta'
        self.canal = canal
        self.volume = 10
        self.estado =  estado
    def mudar_canal(self, novo_canal):
        self.canal = novo_canal

    def mudar_volume(self, novo_volume):
        self.volume = novo_volume

    def ligar_desligar(self):
        pass

    def mostrar_canal(self):
        pass


tv_da_sala = TV('Globo', 'Ligada')
print(tv_da_sala.volume)
tv_da_sala.mudar_volume(40)
print(tv_da_sala.volume)
print(tv_da_sala.canal) # Netflix
tv_da_sala.mudar_canal('Disney Plus')
print(tv_da_sala.canal)


