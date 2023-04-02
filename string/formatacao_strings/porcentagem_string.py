
"""  Formato Percentual"""

print()
print('-'*20, '   CASO 1   ', '-'*20)
print()
custo = 500
faturamento = 1300
lucro =  faturamento - custo
margem = lucro / faturamento
# A margem de lucro foi de 61.54%
print('A margem de lucro foi de {:.2%}'.format(margem))