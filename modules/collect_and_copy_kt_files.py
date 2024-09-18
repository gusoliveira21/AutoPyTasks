import os
import shutil

def collect_and_copy_kt_files(source_dir, target_dir):
    # Criando o diretório de destino, se ele não existir
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith(".kt"):
                source_file_path = os.path.join(root, file)
                target_file_path = os.path.join(target_dir, file)

                # Verificando e resolvendo conflitos de nome de arquivo
                base_name, extension = os.path.splitext(file)
                counter = 1
                while os.path.exists(target_file_path):
                    new_file_name = f"{base_name}_{counter}{extension}"
                    target_file_path = os.path.join(target_dir, new_file_name)
                    counter += 1

                # Copiando o arquivo
                shutil.copy(source_file_path, target_file_path)

# Solicitando a URI do usuário
source_directory = input("Digite o caminho do diretório fonte: ")
target_directory = "C:\\Users\\Alabia\\Downloads\\kolin_files"

# Executando a função
collect_and_copy_kt_files(source_directory, target_directory)
