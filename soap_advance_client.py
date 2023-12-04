# Python
from zeep import Client

# Create a client for the SOAP service
client = Client('http://localhost:8000/?wsdl')

# Call the get_book operation
result = client.service.get_book(1)
print(result)

# Call the get_all_books operation
result = client.service.get_all_books()
print(result)