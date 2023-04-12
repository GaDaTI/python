class Funcionario:
    def regitra_horas(self):
        print('FUNCIONARIO DIZ:  Horas registradas')

    def mostrar_tarefas(self):
        print('FUNCIONARIO DIZ: Fez muitas coisas ... ')


class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('CAELUM DIZ: Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'CAELUM DIZ: Mostrando cursos - {mes} ' if mes else 'Mostrando cursos desse mês ')


class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('ALURA DIZ: Fez muita coisa, Alurete')

    def busca_perguntas_sem_resposta(self):
        print('ALURA DIZ:  Mostrando perguntas não respondidas do forum')


class Junior(Alura):
    pass


class Pleno(Alura, Caelum):
    pass


if __name__ == '__main__' :
    print()
    print()
    print('-' * 80)
    print('# Criação do objeto')
    print('-' * 80)
    print()
    print('jose =  Junior()')
    print()
    jose =  Junior()
    print('-'*80)
    print('# Herdando metodo da classe mãe')
    print('-' * 80)
    print()
    print('jose.regitra_horas()')
    print()
    jose.regitra_horas()
    print()
    print('-' * 80)
    print('#Propia classe')
    print('-' * 80)
    print()
    jose.mostrar_tarefas()
    jose.busca_perguntas_sem_resposta()
    print()
    print('-' * 80)
    print('#busca_cursos_do_mes')
    print('-' * 80)
    print()
    # jose.buscar_curso_do_mes()
    print('jose.buscar_curso_do_mes()')
    print('Resultado esperado uma vez que o metodo faz parte de uma outra classe"')
    print('AttributeError: "Junior" object has no attribute "buscar_curso_do_mes"')
    print()
    print('-' * 80)
    print('# Criação do objeto')
    print('-' * 80)
    print()
    print('thiago = Pleno(Alura, Caelum)')
    print()
    thiago = Pleno()
    print()
    print('# thiago.busca_perguntas_sem_resposta()')
    thiago.busca_perguntas_sem_resposta()
    print()
    print('# thiago.mostrar_tarefas()')
    thiago.mostrar_tarefas()
    print()




