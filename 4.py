# Método Delete

import requests

print("Iniciando requisição.")

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.delete(url)

print("Requisição feita!")

if response.status_code == 200:
    print("Post deletado com sucesso!")

else:
    print(f"Erro ao deletar o post: {response.status_code}")