import os
import re

def remove_comments_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            # Remove line comments
            content = re.sub(r'(?m)^ *//.*\n?', '', content)
            # Remove block comments
            content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
    except PermissionError as e:
        print(f"Erro de permissão ao tentar processar o arquivo: {file_path}. Erro: {e}")
    except Exception as e:
        print(f"Erro ao processar o arquivo: {file_path}. Erro: {e}")

def should_ignore_file(file_name):
    return file_name.startswith('.') or 'cache' in file_name.lower() or 'trash' in file_name.lower()

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if not should_ignore_file(d)]  # Modifica dirs in-place para excluir diretórios ignorados
        for file_name in files:
            if should_ignore_file(file_name):
                continue
            if file_name.endswith('.kt') or file_name.endswith('.kts'):  # Assumindo que arquivos Kotlin têm extensões .kt ou .kts
                file_path = os.path.join(root, file_name)
                remove_comments_from_file(file_path)

if __name__ == '__main__':
    uri = input("Digite o caminho do diretório: ")
    if os.path.isdir(uri):
        process_directory(uri)
    else:
        print(f"O caminho fornecido não é um diretório: {uri}")
