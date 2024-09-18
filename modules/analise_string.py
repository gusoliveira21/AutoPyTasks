import re
from collections import Counter

def extrair_strings_repetidas(caminho_arquivo):
    # Abre e lê o arquivo local
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        texto = arquivo.read()

    # Encontra todas as strings entre aspas
    strings_entre_aspas = re.findall(r'"(.*?)"', texto)

    # Conta cada string e identifica as repetidas
    contador = Counter(strings_entre_aspas)
    strings_repetidas = {string: contagem for string, contagem in contador.items() if contagem > 1}

    return strings_repetidas

# Caminho para o arquivo local
caminho_arquivo = "C:/Users/Alabia/Downloads/codigo.txt"

# Executa a função e imprime as strings repetidas
strings_repetidas = extrair_strings_repetidas(caminho_arquivo)
print(strings_repetidas)
