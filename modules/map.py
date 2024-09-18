import os


def mapear_pasta(uri, nome_arquivo):
    nome_arquivo = f"{nome_arquivo}.txt"
    
    with open(nome_arquivo, 'w') as arquivo:
        for dirpath, dirnames, filenames in os.walk(uri):

            # Ignora diretórios __pycache__
            if '__pycache__' in dirpath:
                continue
            
            for f in filenames:
                # Ignora arquivos dentro de diretórios __pycache__
                if '__pycache__' in f:
                    continue

                caminho_completo = os.path.join(dirpath, f)
                arquivo.write(caminho_completo + '\n')
                
                with open(caminho_completo, 'r', errors='replace') as file:
                    try:
                        conteudo = file.read()
                        arquivo.write(conteudo + '\n')
                    except Exception as e:
                        arquivo.write(f"Erro ao ler o arquivo: {e}\n")

                arquivo.write('-' * 50 + '\n')

if __name__ == "__main__":
    #uri = "C:\\Users\\Gustavo\\Documents\\Studio\\PetJournal\\petJournal\\petjournal.android\\petJournal\\data\\src\\main\\java\\com\\soujunior\\data"
    #"C:\\Users\\Alabia\\OneDrive\\Documentos\\Studio\\Alabia\\PythonStudy\\ManagerRobots\\project_app"
    uri = input("Digite a URI da pasta que você deseja mapear: ")
    nome_arquivo = input("Digite o nome base do arquivo onde as informações serão salvas (sem a extensão .txt): ")
    mapear_pasta(uri, nome_arquivo)
    print(f"Informações salvas em {nome_arquivo}.txt")
