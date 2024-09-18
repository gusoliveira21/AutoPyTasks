import os
import zipfile
import shutil

def zip_directory(source_dir, zip_dir, max_size_mb=24):
    max_size = max_size_mb * 1024 * 1024  # Convertendo MB para bytes
    current_zip = None
    current_zip_size = 0
    zip_index = 1

    for root, dirs, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)

            # Abrindo novo arquivo ZIP se necessário
            if not current_zip or current_zip_size + file_size > max_size:
                if current_zip:
                    current_zip.close()

                zip_path = os.path.join(zip_dir, f"{os.path.basename(source_dir)}_{zip_index}.zip")
                current_zip = zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED)
                current_zip_size = 0
                zip_index += 1

            # Adicionando arquivo ao arquivo ZIP
            arcname = os.path.relpath(file_path, source_dir)
            current_zip.write(file_path, arcname)
            current_zip_size += file_size

    if current_zip:
        current_zip.close()

# Solicitando a URI do usuário
source_directory = input("Digite o caminho do diretório fonte: ")

# Executando a função para cada pasta dentro do diretório
for item in os.listdir(source_directory):
    item_path = os.path.join(source_directory, item)
    if os.path.isdir(item_path):
        zip_directory(item_path, source_directory)
