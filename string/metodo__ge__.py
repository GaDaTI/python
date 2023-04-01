"""
O método __ge__ é um método especial da classe string em Python que é usado para verificar se uma string é maior ou igual a
 outra em ordem lexicográfica.
"""
str_1 = "banana"
str_2 = "abacaxi"

print(len(str_1)) # 6
print(len(str_2)) # 7
print(str_1.__ge__(str_2))
print(str_2.__ge__(str_1))

str_1 = "abacaxi"
str_2 = "abacaxi"

print(len(str_1)) # 6
print(len(str_2)) # 7
print(str_1.__ge__(str_2))
print(str_2.__ge__(str_1))