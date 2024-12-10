# Método get

import requests

print("Iniciando requisição.")

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

print("Requisição feita!")

if response.status_code == 200:
    print("Requisição bem-sucedida!")
    data = response.json()
    for post in data[:5]:
        print(f"ID do usuário: {post['userId']}, ID: {post['id']}, Título: {post['title']}, Corpo: {post['body']}")

else:
    print(f"Erro na requisição: {response.status_code}")