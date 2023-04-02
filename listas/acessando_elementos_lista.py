"""   FATIAMENTO  COM LISTA  """

# Acessando elementos de uma lista : o elemento da lista pode ser acessado usando a estrutura TEXTO[POSIÇÃO]
produtos = ['TV', 'Celular', 'mouse', 'teclado', 'tablet']
print(produtos[1]) # TV
print(produtos[4]) # tablet

# Acessando elementos de duas  listas com informações complementares
produtos = ['TV', 'Celular', 'mouse', 'teclado', 'tablet']
vendas = [1000, 1500, 345, 234, 877]
texto = 'As vendas de {} foram de {}'.format(produtos[1],vendas[2])
print(texto)