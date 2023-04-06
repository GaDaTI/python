from class_pessoa import  Pessoa

washington = Pessoa('Washington', 'Ruan', '18', '23', '08', '2005', 'Solteiro','Salvador', 'BA')

if __name__ == '__main__' :
    for keys, value in washington.__dict__.items():
        print(keys)