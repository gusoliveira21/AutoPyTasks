import json
import os

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
            return data
        except FileNotFoundError:
            print("Arquivo não encontrado. Por favor, insira um caminho válido.")
        except json.JSONDecodeError:
            print("Erro ao decodificar JSON. Por favor, insira um arquivo JSON válido.")

# Chamada da função
json_data = read_json_file()

# Imprimir os 10 primeiros itens do JSON de forma formatada
print(json.dumps(json_data[:10], indent=4))
