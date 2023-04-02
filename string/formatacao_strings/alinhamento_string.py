print()
print(""" ALINHAMENTO DE  STRINGS """)
print()
print('-'*80)
# 1. Formato padrão sem alinhamento
email = 'gabriel@gmail.com'

#Meu e-mail não é gabriel@gmail.com, show ?
print('Meu e-mail não é {}, show ?'.format(email))
print()
print('-'*80)
# 2. Caixa de texto com tamanho de 30 caracteres e texto alinhado à esquerda ( : < )
# Meu e-mail não é gabriel@gmail.com             , show ?
print('Meu e-mail não é {:<30}, show ?'.format(email))
print(f"Meu e-mail não é {email:<30}, show ?")
print()
print('-'*80)
# 3. Caixa de texto com tamanho de 30 caracteres e texto alinhado à direita (:>)
# Meu e-mail não é gabriel@gmail.com             , show ?
print('Meu e-mail não é {:>30}, show ?'.format(email))
print(f"Meu e-mail não é {email:>30}, show ?")
print()
print('-'*80)
# 4. Caixa de texto com tamanho de 30 caracteres e texto centralizado(:^)
#Meu e-mail não é       gabriel@gmail.com       , show ?
print('Meu e-mail não é {:^30}, show ?'.format(email))
print(f"Meu e-mail não é {email:^30}, show ?")