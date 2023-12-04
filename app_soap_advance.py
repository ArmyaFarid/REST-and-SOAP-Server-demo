# Python
from spyne import Application, rpc, ServiceBase, \
    Integer, Unicode, ComplexModel
from spyne import Iterable
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server


# Define a complex type
class Book(ComplexModel):
    id = Integer
    title = Unicode
    author = Unicode

class BookService(ServiceBase):
    # Define an operation that returns a book
    @rpc(Integer, _returns=Book)
    def get_book(ctx, id):
        # In a real application, you would get the book from a database
        return Book(id=id, title="Example Book", author="Example Author")

    # Define an operation that returns multiple books
    @rpc(_returns=Iterable(Book))
    def get_all_books(ctx):
        # In a real application, you would get the books from a database
        return [
            Book(id=1, title="Example Book 1", author="Example Author 1"),
            Book(id=2, title="Example Book 2", author="Example Author 2"),
        ]

# Create a SOAP application
application = Application([BookService], 'spyne.examples.books.soap',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

# Wrap the Spyne application with its wsgi wrapper
wsgi_application = WsgiApplication(application)


if __name__ == '__main__':
    # Create a WSGI server and run it
    server = make_server('localhost', 8000, wsgi_application)
    server.serve_forever()