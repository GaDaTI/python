"""
O método __doc__ é um método especial da classe string em Python que retorna a documentação da classe ou do objeto.
Ele é usado para recuperar a string de documentação associada a uma classe ou a um objeto específico.
"""
class Pessoa:
    """
    Essa é uma classe que representa uma pessoa.
    Ela tem um atributo 'nome' e um método 'dizer_oi'
    que imprime uma saudação na tela.
    """

    def __init__(self, nome):
        self.nome = nome

    def dizer_oi(self):
        print(f"Olá, meu nome é {self.nome}!")

print(Pessoa.__doc__)