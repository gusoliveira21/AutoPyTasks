import json
import os

# Define uma classe Kotlin correspondente à estrutura do JSON
class MyPOJO:
    def __init__(self, key1, key2):
        self.key1 = key1
        self.key2 = key2

def read_json_file():
    while True:
        # Solicita ao usuário a entrada do caminho do arquivo JSON
        file_path = input("Por favor, insira o caminho do arquivo JSON: ")

        # Verifica se o caminho termina com '.json'
        if not file_path.endswith('.json'):
            print("A rota não condiz com um arquivo JSON.")
            continue

        # Tenta abrir e ler o arquivo JSON
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
            
            # Verifica se as chaves necessárias existem no JSON
            if 'key1' in data and 'key2' in data:
                # Cria um objeto MyPOJO a partir do JSON
                pojo = MyPOJO(data['key1'], data['key2'])
                return pojo
            else:
                print("O JSON não possui as chaves necessárias.")
        except FileNotFoundError:
            print("Arquivo não encontrado. Por favor, insira um caminho válido.")
        except json.JSONDecodeError:
            print("Erro ao decodificar JSON. Por favor, insira um arquivo JSON válido.")

# Chamada da função
kotlin_pojo = read_json_file()

# Você pode acessar os campos do objeto Kotlin assim:
print("key1:", kotlin_pojo.key1)
print("key2:", kotlin_pojo.key2)
