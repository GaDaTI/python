"""   Casas Decimais  """

print()
print('-'*20, '   CASO 1   ', '-'*20)
print()
custo = 5000
faturamento = 2700
lucro =  faturamento - custo
# Faturamento foi 2,700.000000 e o lucro -2,300.000000
print('Faturamento foi {:,f} e o lucro {:,f}'.format(faturamento, lucro))

print()
print('-'*20, '   CASO 2 : Limitando o numero de casas decimais   ', '-'*20)
print()
custo = 5000
faturamento = 2700
lucro =  faturamento - custo
# Faturamento foi 2,700.000000 e o lucro -2,300.000000
print('Faturamento foi {:.2f} e o lucro {:.2f}'.format(faturamento, lucro))