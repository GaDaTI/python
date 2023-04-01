"""
O método __eq__ é um método especial da classe string em Python que é usado para verificar se duas strings são iguais.
"""
str_1 = "Paulo"
str_2 = "Humberto"
str_3 = "Paulo"
str_4 = "paulo"

print(str_1.__eq__(str_2)) # False

print(str_1.__eq__(str_3)) # True

print(str_1.__eq__(str_4)) # False