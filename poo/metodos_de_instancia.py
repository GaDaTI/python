"""  Introdução aos métodos Python"""
# Metodo é uma função vinculada a uma instancia de classe.

class Request:
    def send():
        print('Sent')


# Chamando a função send()
Request.send() # Sent

# send() é um objeto de função , que é uma instancia da classe function
print(Request.send) #<function Request.send at 0x7f35b942aef0>

# Tipo de send()
print(type(Request.send)) # <class 'function'>

# Criando um objeto com classe Request retorna um objeto de método vinculado
http_request = Request()
print(http_request.send) # <bound method Request.send of <__main__.Request object at 0x7f4522bf7370>>











