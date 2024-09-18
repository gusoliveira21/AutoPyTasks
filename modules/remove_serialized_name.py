import re

def remove_serialized_name_from_file(filepath):
    try:
        with open(filepath, "r") as file:
            lines = file.readlines()

        found = False
        with open(filepath, "w") as file:
            for line in lines:
                # Regex mais abrangente
                if re.search(r'@SerializedName\("[^"]+"\)', line):
                    found = True
                    print("Removendo linha:", line.strip())
                    continue
                file.write(line)
        
        if not found:
            print("Nenhuma linha com @SerializedName encontrada.")
            # Adicionando depuração para verificar as primeiras linhas do arquivo
            print("Verificando as primeiras 5 linhas do arquivo:")
            for line in lines[:15]:
                print(line.strip())

    except FileNotFoundError:
        print("Arquivo não encontrado:", filepath)
    except Exception as e:
        print("Ocorreu um erro:", e)

# Pedindo ao usuário para inserir o caminho do arquivo
file_path = input("Por favor, insira o caminho do arquivo: ")
remove_serialized_name_from_file(file_path)
