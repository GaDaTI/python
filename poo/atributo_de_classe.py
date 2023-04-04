# Introdução às variáveis (atributos) de classe do Python

# Quando você define uma classe usando a classpalavra-chave, o Python cria um objeto com o mesmo nome da classe. Por exemplo:
class HtmlDocument5:
    pass


print(HtmlDocument5.__name__)  # objeto: HtmlDocument

# E HtmlDocument tem o tipo de type:
print(type(HtmlDocument5))  # <class 'type'>

# Também é uma instaância da classe type
print(isinstance(HtmlDocument5, type))  # True

""" ATRIBUTO DE CLASSE """


# extension, version estão vinculados à HtmlDocumentclasse.
class HtmlDocument:
    extension = 'html'
    version = '5'


""" ATRIBUTO DE CLASSE:  ACESSANDO VALORES DOS ATRIBUTOS DE CLASSE """
# Forma 1 : Acessando os valores dos atributos de classe
print(HtmlDocument.extension)  # html
print(HtmlDocument.version)  # 5

# Forma  2 : Acessando os valores dos atributos de classe pelo metodo getattr()
valor_da_extension = getattr(HtmlDocument, 'extension')
valor_da_version = getattr(HtmlDocument, 'version')
print('Valor do atributo de classe extension: {}'.format(valor_da_extension))
print('Valor do atributo de classe version: {}'.format(valor_da_version))

""" ATRIBUTO DE CLASSE:  TENTANDO ACESSAR  VALORES DE ATRIBUTOS DE CLASSE INEXISTENTE"""
# Acessando  atributos de classe inexistente
# AttributeError: type object 'HtmlDocument' has no attribute 'media_type'
# print(HtmlDocument.media_type)

""" ATRIBUTO DE CLASSE:  ATRIBUINDO  VALORES PARA ATRIBUTOS DE CLASSE  """
# Definir valores para os atributos de classe
# Forma  1 : Atribuindo um valor para atributos de classe
print(HtmlDocument.version)  # 5
HtmlDocument.version = 10
print(HtmlDocument.version)  # 10

# Forma  2 : Atribuindo um valor a atributos de classe  pelo metodo setattr()
print(HtmlDocument.version)  # 10
setattr(HtmlDocument, 'version', 5)
print(HtmlDocument.version)  # 5

""" ATRIBUTO DE CLASSE:  CRIANDO ATRIBUTOS DE CLASSE  """
# AttributeError: type object 'HtmlDocument' has no attribute 'media_type'
# print(HtmlDocument.media_type)
HtmlDocument.media_type = 'text/html'
print(HtmlDocument.media_type)  # text/html

""" ATRIBUTO DE CLASSE:  EXCLUIR ATRIBUTOS DE CLASSE  """


class HtmlDocument7:
    extension = 'html'
    version = '5'


print(HtmlDocument7.version)
delattr(HtmlDocument7, 'version')
# AttributeError: type object 'HtmlDocument7' has no attribute 'version'
# print(HtmlDocument7.version)

""" ATRIBUTO DE CLASSE:  ARMAZENAMENTO ATRIBUTOS DE CLASSE  """
from pprint import pprint


class HtmlDocument23:
    extension = 'html23'
    version = '23'


HtmlDocument23.media_type = 'text/html'

pprint(HtmlDocument23.__dict__)
"""  
Conforme mostrado claramente na saída, o __dict__possui três variáveis de classe: extension, media_type e version além de outras 
variáveis  de classe predefinidas.

mappingproxy({'__dict__': <attribute '__dict__' of 'HtmlDocument23' objects>,
              '__doc__': None,
              '__module__': '__main__',
              '__weakref__': <attribute '__weakref__' of 'HtmlDocument23' objects>,
              'extension': 'html23',
              'media_type': 'text/html',
              'version': '23'})
"""

print("HtmlDocument23.__dict__['released'] = 2008")
# HtmlDocument23.__dict__['released'] = 2008 => TypeError: 'mappingproxy' object does not support item assignment
"""
Traceback (most recent call last):
  File "/home/gabriel/Documents/developer/servidor/hashtag/poo/intro_atribuilt_class.py", line 90, in <module>
    HtmlDocument23.__dict__['released'] = 2008
TypeError: 'mappingproxy' object does not support item assignment

"""

""" ATRIBUTO DE CLASSE:  CALLEBLE CLASS ATTRIBUTES """
from pprint import pprint


class HtmlDocument78:
    extension = 'html78'
    version = '78'

    def render():
        print('Redering the html doc....')


pprint(HtmlDocument78.__dict__)

"""
mappingproxy({'__dict__': <attribute '__dict__' of 'HtmlDocument78' objects>,
              '__doc__': None,
              '__module__': '__main__',
              '__weakref__': <attribute '__weakref__' of 'HtmlDocument78' objects>,
              'extension': 'html78',
              'render': <function HtmlDocument78.render at 0x7efdc4c8b130>,
              'version': '78'})


"""
#Resumo:
#Uma classe é um objeto que é uma instância do tipo classe.
#Variáveis de classe são atributos do objeto de classe.
#Use notação de ponto ou getattr()função para obter o valor de um atributo de classe.
#Use notação de ponto ou setattr()função para definir o valor de um atributo de classe.
#Python é uma linguagem dinâmica. Portanto, você pode atribuir uma variável de classe a uma classe em tempo de execução.
#Python armazena variáveis de classe no __dict__atributo. O __dict__atributo é um dicionário.
