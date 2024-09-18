import os

def replace_in_file(file_path, term_a, term_b):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        content = content.replace(term_a, term_b)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
    except Exception as e:
        print(f'Erro ao processar o arquivo {file_path}: {e}')

def main():
    term_a = input('Digite o termo A: ')
    term_b = input('Digite o termo B: ')
    uri = input('Digite a URI do diretório: ')

    for dirpath, dirnames, filenames in os.walk(uri, topdown=False):
        for dirname in dirnames:
            if term_a in dirname:
                new_dirname = dirname.replace(term_a, term_b)
                os.rename(os.path.join(dirpath, dirname), os.path.join(dirpath, new_dirname))
        for filename in filenames:
            if term_a in filename:
                new_filename = filename.replace(term_a, term_b)
                os.rename(os.path.join(dirpath, filename), os.path.join(dirpath, new_filename))
            file_path = os.path.join(dirpath, filename)
            replace_in_file(file_path, term_a, term_b)

if __name__ == '__main__':
    main()
