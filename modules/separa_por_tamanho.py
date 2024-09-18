import os
import shutil

def move_kt_files_based_on_size(source_dir):
    # Definindo as pastas de destino
    small_files_dir = os.path.join(source_dir, "pequeno")
    large_files_dir = os.path.join(source_dir, "grande")

    # Criando as pastas de destino, se não existirem
    os.makedirs(small_files_dir, exist_ok=True)
    os.makedirs(large_files_dir, exist_ok=True)

    # Tamanho limite para arquivos pequenos (24 MB)
    size_limit = 24 * 1024 * 1024

    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith(".kt"):
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)

                # Movendo o arquivo para a pasta correspondente
                if file_size <= size_limit:
                    shutil.move(file_path, os.path.join(small_files_dir, file))
                else:
                    shutil.move(file_path, os.path.join(large_files_dir, file))

# Solicitando a URI do usuário
source_directory = input("Digite o caminho do diretório fonte: ")

# Executando a função
move_kt_files_based_on_size(source_directory)
