""" Edição de Sinal"""
print()
print('-'*20, '   CASO 1   ', '-'*20)
print()
custo = 500
faturamento = 270
lucro =  faturamento - custo
# CASO 1 : lucro =   faturamento - custo
# Faturamento foi 270 e lucro -230
print('Faturamento foi {} e o lucro {}'.format(faturamento, lucro))
print()
print('-'*20, '   CASO 2   ', '-'*20)
print()
custo = 500
faturamento = 270
lucro =   faturamento - custo
# CASO  2 : lucro =   custo - faturamento
# Faturamento foi 270 e lucro -230
print('Faturamento foi {:+} e o lucro {:+}'.format(faturamento, lucro))



