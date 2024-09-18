import os
import shutil

def create_grouped_folders(source_dir, max_size_mb=24):
    max_size = max_size_mb * 1024 * 1024  # Convertendo MB para bytes
    current_folder_size = 0
    current_folder_index = 1
    current_folder_path = os.path.join(source_dir, f"group_{current_folder_index}")

    os.makedirs(current_folder_path, exist_ok=True)

    for root, dirs, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)

            # Verificando se a adição do arquivo atual ultrapassará o limite de tamanho
            if current_folder_size + file_size > max_size:
                current_folder_index += 1
                current_folder_path = os.path.join(source_dir, f"group_{current_folder_index}")
                os.makedirs(current_folder_path, exist_ok=True)
                current_folder_size = 0

            # Movendo o arquivo para a pasta atual
            shutil.move(file_path, os.path.join(current_folder_path, file))
            current_folder_size += file_size

# Solicitando a URI do usuário
source_directory = input("Digite o caminho do diretório fonte: ")

# Executando a função
create_grouped_folders(source_directory)
