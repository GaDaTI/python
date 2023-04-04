"""  Introdução às variáveis de instância do Python """

#  As variáveis  de classe são vinculadas a uma classe
#  As variáveis de instância são vinculadas a uma instância específica de uma classe
from pprint import pprint

#class HtmlDocument:
#    version = 5
#    extension = 'html'


#pprint(HtmlDocument.__dict__)

""" Python armazena essas duas variáveis no __dict__atributo:

mappingproxy({'__dict__': <attribute '__dict__' of 'HtmlDocument' objects>,
              '__doc__': None,
              '__module__': '__main__',
              '__weakref__': <attribute '__weakref__' of 'HtmlDocument' objects>,
              'extension': 'html',
              'version': 5})
"""
#Quando você acessa as variáveis  de classe por meio da classe,
# o Python as procura no arquivo __dict__da classe.
#print(HtmlDocument.version)
#print(HtmlDocument.extension)

# O homeé uma instância da HtmlDocumentclasse. Tem seu próprio __dict__atributo:
##home = HtmlDocument()
#pprint(home.__dict__) # { } -> Retorna um __dict__ vazio

# Ao contrário do __dict__atributo de uma classe, o tipo do __dict__atributo de uma instância é um dicionário .
#print(type(HtmlDocument.__dict__)) # <class 'mappingproxy'>
#print(type(home.__dict__)) # <class 'dict'>

"""  ACESSANDO OS ATRIBUTOS DE CLASSE DE UMA INSTANCIA """
#print(home.extension) # html
#print(home.version) # 5

# Redefinindo o valor do atributo de classe de uma instancia
#home.version = 4
#print(home.version) # 4
#pprint(home.__dict__) # {'version': 4}
#home.version = 8
#print(home.version) # 8
#pprint(home.__dict__) # {'version': 8}

"""  ALTERANDO ATRIBUTOS DE CLASSE REFLETIRÃO NAS INSTÂNCIAS DA CLASSE """
class HtmlDocument5:
    version = 5
    extension = 'html'

home_site = HtmlDocument5()

HtmlDocument5.media_type = 'text/html'

print(home_site.media_type) # text/html