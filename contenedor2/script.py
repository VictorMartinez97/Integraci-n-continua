import requests

response = requests.get('http://contenedor1:5000')
print("Response from Contenedor 1:", response.text)
