# Python
from spyne import Application, rpc, ServiceBase, Integer
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

class MySoapService(ServiceBase):
    @rpc(Integer, Integer, _returns=Integer)
    def add_numbers(ctx, num1, num2):
        return num1 + num2

class MyOtherSoapService(ServiceBase):
    @rpc(Integer, Integer, _returns=Integer)
    def multiply_numbers(ctx, num1, num2):
        return num1 * num2

application = Application([MySoapService, MyOtherSoapService], 'my_namespace',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    server = make_server('localhost', 5001, wsgi_application)
    server.serve_forever()