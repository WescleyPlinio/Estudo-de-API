# Método put

import requests

print("Iniciando requisição.")

url = "https://jsonplaceholder.typicode.com/posts/1"

dados_atualizados = {
    "title": "Título atualizado",
    "body": "Este post foi atualizado com sucesso!",
    "userId": 1
}
print("Requisição feita!")


response = requests.put(url, json = dados_atualizados)

if response.status_code == 200:
    print("Post atualizado com sucesso!")
    print("Resposta do servidor:")
    print(response.json())
else:
    print(f"Erro ao atualizar o post: {response.status_code}")