"""
Módulo 7 – Strings

"""

# 7.1.1 STRINGs no Python são listas:

"""
|  0  |  1  |  2  | 3  |  4  |  5  |  6    |  7   |  8  |   9    | 10  | 11  | 12  |   13   |  14  |   15    |   16  |
|  g  |  a  |  b  |  r  |   i  |  e  |   l    |  @  |  g  |   m   |  a   |   i    |  l    |      .    |    c  |     o     |    m  |
"""

# 7.2 Índice e tamanho da String
email ='gabriel@gmail.com'
print(email)
email.strip()

# Tamanho da string
print(len(email))

# Acessando o indice de [ 0 a 7 ]  = 'gabriel'
print(email[:7])

# <class 'str'>
print(type(email.strip()))

# 7.3 Índice Negativo e Pedaço de String
# gabriel
print(email[ -17 : -10])

# gabriel
print(email[     : -10])

# 7.4 Operações com String
# 7.4 .1 -  str -> transforma número em string;
numero = 7
print(type(numero), numero) #<class 'int'> 7
numero = str(numero)
print(type(numero), numero) #<class 'str'> 7

# TypeError: can only concatenate str (not "int") to str
faturamento =  2000
custo = 500
lucro = faturamento  -  custo
#print('O faturamento da loja foi de : ' + faturamento)

#O faturamento da loja foi de : 2000
print('O faturamento da loja foi de : ' + str(faturamento))

# 7.4 .2 -  str -> transforma número em string;











# in -> verifica se um texto está contido dentro do outro

