"""
casefold -> Transforma todas as letras Maíusculas em Minusculas

casefold()  x lower()
seguindo as regras do alfabeto ASCII padrão.
"""
comida= "SaRaPaTeL"
print(comida)

print(comida.casefold())

print(comida)

print(comida.lower())

texto = "MAISON BLANCHE"
print(texto.lower())      # saída: "ação de graças"
print(texto.casefold())   # saída: "ação de graças"