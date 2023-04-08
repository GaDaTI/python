from class_pessoa import Pessoa
from rg import  RegistroCivil


class PessoaMae(RegistroCivil):

    def __init__(self):
        PessoaMae.filho.append(self.filho)

