"""
O método __contains__ é usado na classe string do Python para verificar se uma determinada substring está presente na string principal.
"""
email = "gabriel@gmail.com "


print(email.__contains__("@")) # Retorna: True

print(email.__contains__("G")) # Retorna:  False

print(email.__contains__("g")) # Retorna:  True

