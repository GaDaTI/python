"""
Cria uma lista, onde cada item é o texto de uma linha. Cada “ENTER” é criado um novo item na lista.
"""

texto = '''Olá , bom dia.
Venho por meio desse e-mail lhe informar o faturamento da loja no dia de hoje.
Faturamento = R$ 2.500,00 '''

print(texto)
print('-'*50)
documentacao = texto.splitlines()
print(texto.splitlines())
print('-'*50)
