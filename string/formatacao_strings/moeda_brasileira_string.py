"""  Formato  Moeda"""

print()
print('-'*20, '   CASO 1   ', '-'*20)
print()

custo = 500
faturamento = 2700
lucro = faturamento - custo
# R$ 2.200,00
lucro_str ='R$ {:_.2f}'.format(lucro)
print(lucro_str.replace('.' , ',').replace('_','.'))