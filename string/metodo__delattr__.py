"""
O método __delattr__ é um método especial da classe Python que é chamado quando o operador del é usado para excluir um atributo
de um objeto.
Quando você usa o operador del para excluir um atributo de um objeto, o Python procura o método __delattr__ na classe do objeto e
chama esse método se ele existir. O método recebe dois parâmetros: self, que é a instância do objeto, e name, que é uma string contendo
o nome do atributo a ser excluído.
"""
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def __delattr__(self, name):
        print(f"O atributo {name} foi excluído.")
        super().__delattr__(name)

p = Pessoa("João")
del p.nome
