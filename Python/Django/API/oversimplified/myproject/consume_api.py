import requests

response = requests.get('http://localhost:8000/')
# response = requests.post('http://localhost:8000/add/', data={'name': 'New Item'})
print(response.json())
