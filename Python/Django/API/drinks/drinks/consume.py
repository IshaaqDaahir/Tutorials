import requests

response = requests.get('http://localhost:8000/drinks/')
print(response.json())