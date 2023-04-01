"""
O método __delattr__ é um método especial da classe Python que é chamado quando o operador del é usado para excluir um atributo
de um objeto.
Quando você usa o operador del para excluir um atributo de um objeto, o Python procura o método __delattr__ na classe do objeto e
chama esse método se ele existir. O método recebe dois parâmetros: self, que é a instância do objeto, e name, que é uma string contendo
o nome do atributo a ser excluído.
"""
class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    def __delattr__(self, name):
        print(f"O atributo {name} foi excluído.")
        super().__delattr__(name)


""" CASO 1 """
aluno = Pessoa()

print(aluno.nome) # None
print(aluno.idade) # None
del aluno.nome
print(aluno.nome) # AttributeError: 'Pessoa' object has no attribute 'nome'
aluno.nome = "Paulo"
aluno.idade = 23
print(aluno.nome) # Paulo
print(aluno.idade) # 23


