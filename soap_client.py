# Python
from zeep import Client

# Create a client for the SOAP service
client = Client('http://localhost:5001/?wsdl')

# Call the add_numbers operation
result = client.service.add_numbers(5, 3)

# Print the result
print(result)

# Call the multiply_numbers operation
result = client.service.multiply_numbers(5, 3)

#print the result
print(result)