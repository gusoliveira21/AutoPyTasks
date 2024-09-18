from pydub import AudioSegment
import os
import glob

def amplify_audio(input_file, output_file, amplification_db):
    """
    Amplifica o volume de um arquivo de áudio.
    
    :param input_file: Caminho para o arquivo de entrada.
    :param output_file: Caminho para salvar o arquivo amplificado.
    :param amplification_db: Quantidade de decibéis para aumentar o volume.
    """
    # Carregar o arquivo de áudio
    audio = AudioSegment.from_file(input_file)
    
    # Amplificar o áudio
    amplified_audio = audio + amplification_db
    
    # Exportar o áudio amplificado
    amplified_audio.export(output_file, format="mp3")
    print(f"Arquivo salvo em: {output_file}")

def process_audio_files(directory, output_directory, amplification_db):
    """
    Processa todos os arquivos de áudio em um diretório, amplifica o volume e salva em um novo diretório.
    
    :param directory: Diretório contendo os arquivos de áudio.
    :param output_directory: Diretório para salvar os arquivos amplificados.
    :param amplification_db: Quantidade de decibéis para aumentar o volume.
    """
    # Verificar se o diretório de saída existe, se não, criar
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    # Encontrar todos os arquivos de áudio no diretório (mp3 e wav)
    audio_files = glob.glob(os.path.join(directory, "*.mp3")) + glob.glob(os.path.join(directory, "*.wav"))
    
    if not audio_files:
        print("Nenhum arquivo de áudio encontrado no diretório.")
        return
    
    for audio_file in audio_files:
        # Nome do arquivo de saída
        output_file = os.path.join(output_directory, os.path.basename(audio_file))
        
        # Amplificar e salvar o arquivo
        amplify_audio(audio_file, output_file, amplification_db)

# Exemplo de uso
input_directory = r"C:\Users\Alabia\Downloads\livreto\audio_amplificado"  # Diretório contendo os arquivos de áudio
output_directory = r"C:\Users\Alabia\Downloads\livreto\audio_amplificado_processed"  # Diretório de saída
amplification_db = 10  # Amplificação em decibéis (aumentar 10 dB)

process_audio_files(input_directory, output_directory, amplification_db)
