

class Endereco:
    def __init__(self, rua, bairro, nome, cidade, estado):
        self.rua = rua
        self.residencia = bairro
        self.bairro = nome
        self.cidade = cidade
        self.estado = estado

    @classmethod
    def endereco_atual(cls):
        return Endereco(rua, bairro, nome, cidade, estado)

    @classmethod
    def endereco_nascimento(cls, rua, bairro, nome, cidade, estado):
        return Endereco(rua, bairro, nome, cidade, estado)

    @classmethod
    def endereco_comercial (cls, rua, bairro, nome, cidade, estado):
        return Endereco(rua, bairro, nome, cidade, estado)












