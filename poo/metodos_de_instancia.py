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
print(type(http_request.send)) # <class 'method'>

# Diferença entre Request.send  e http_request.send
print(type(Request.send) is type(http_request.send)) #False

""" Portanto, quando você define uma função dentro de uma classe, é puramente uma função. No entanto, quando você acessa essa 
função por meio de um objeto, a função se torna um método.
print(type(Request.send)) # <class 'function'>
print(type(http_request.send)) # <class 'method'>
"""

# Chamando a função por mei da classe Request
Request.send() # Sent

# Chamando a função send() por meio do objeto http_request
# http_request.send() #TypeError: Request.send() takes 0 positional arguments but 1 was given

"""" SELF COMO PRIMEIRO PARAMETRO DO METODO """
class RequestNew:
    def send(*args):
        print('Sent', args)

# Chamando a função send() por meida classe é devolvida uma lista vazia
RequestNew.send() # Sent ()

# Chamando a função send() por meida do objeto é devolvida com um valor
http_request_new = RequestNew()

print(hex(id(http_request_new))) # 0x7f5d61f3b7f0
http_request_new.send() # Sent (<__main__.RequestNew object at 0x7f5d61f3b7f0>,)

""" CONCLUSÃO """
"""
O http_requestobjeto é o mesmo que o Python passa para o send()método como o primeiro argumento porque eles têm o mesmo
 endereço de memória. Em outras palavras, você pode acessar a instância da classe como o primeiro argumento dentro do send()
 método:
"""
# Chamda de metodo
http_request_new.send()

# É equivalente a chamada de função
Request.send(http_request_new)

# Por esta razão, um método de um objeto sempre tem o objeto como primeiro argumento. Por convenção, é chamado de self:
class RequestNew:
    def send(self):
        print('Sent', self)


