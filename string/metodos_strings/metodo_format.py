"""
Já falamos sobre ela anteriormente, lembra?
Ela insere o valor de uma variável no termo indicado
por {}. Muito útil para evitar ter que transformar o
formato de cada variável individualmente
"""
faturamento = '1000'
despesa = '2.500'
# O faturamento  da  loja foi de 1000 e a despesa 2.500
print("O faturamento  da  loja foi de {} e a despesa {}".format(faturamento, despesa))

#O faturamento  da  loja foi de 2.500 e a despesa 1000
print("O faturamento  da  loja foi de {1} e a despesa {0}".format(faturamento, despesa))