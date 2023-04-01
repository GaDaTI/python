"""
Retira os caracteres indesejados, como por exemplo, espaços que não agregam valor.
Perceba que no resultado fornecido pelo Python não existem os espaços indesejados.

"""
texto = ' A casa é amarela    '

print(type(texto))
print(len(texto))

texto = texto.strip()

print(len(texto))
print(type(texto))