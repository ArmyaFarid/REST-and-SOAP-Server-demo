# consommer.py
import requests
import json

# URL de base de votre API
base_url = 'http://localhost:5000/api/book'

# Consommer l'endpoint POST pour créer un nouveau livre
# new_book = {
#     'title': 'New Book',
#     'poster': 'http://example.com/new-book.jpg',
#     'summary': 'This is a new book.',
#     'is_available': True,
#     'author_name': 'Author',
#     'author_country': 'Country'
# }
# response = requests.post(base_url, json=new_book)
# print(f'Response: {response.json()}')

# Consommer l'endpoint GET pour obtenir la liste des livres
response = requests.get(base_url)
books = response.json()
print(f'Books: {json.dumps(books, indent=2)}')

# Consommer l'endpoint GET pour obtenir un livre par son ID
# book_id = 1
# response = requests.get(f'{base_url}/{book_id}')
# book = response.json()
# print(f'Book: {json.dumps(book, indent=2)}')

# Consommer l'endpoint PUT pour mettre à jour un livre
# updated_book = {
#     'title': 'Updated Book'
# }
# response = requests.put(f'{base_url}/{book_id}', json=updated_book)
# print(f'Response: {response.json()}')

# Consommer l'endpoint DELETE pour supprimer un livre
# response = requests.delete(f'{base_url}/{book_id}')
# print(f'Response: {response.json()}')