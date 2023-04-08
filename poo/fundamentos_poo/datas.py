


class Data:

    def __init__(self,  dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.data_str = None

    def formatada(self):
        return print(f" {self.dia} / {self.mes} /  {self.ano}")


if __name__ == '__main__'  :
    data =  Data(8, 4,2023)
    data.formatada()











