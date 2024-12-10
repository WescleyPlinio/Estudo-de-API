# Método post

import requests

print("Iniciando requisição.")

url = "https://jsonplaceholder.typicode.com/posts"

novo_post = {
    "title" : "Plataforma dos projetos integradores",
    "body" : "O PPI é um bom projeto.",
    "userId" : 77,
}

response = requests.post(url, json = novo_post)

print("Requisição feita!")

if response.status_code == 201:
    print("Post created successfully")
    print("Server anwser:")
    print(response.json())

else:
    print(f"Erro no post: {response.status_code}")