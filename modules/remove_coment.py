import re

# Solicita o caminho do arquivo ao usuário
file_path = input('Digite o caminho do arquivo Kotlin: ')

with open(file_path, 'r') as file:
    content = file.read()

# Remove comentários de linha única
content = re.sub(r'//.*', '', content)

# Remove comentários de múltiplas linhas
content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)

# Salva o conteúdo modificado no mesmo arquivo
with open(file_path, 'w') as file:
    file.write(content)

print('Comentários removidos com sucesso!')