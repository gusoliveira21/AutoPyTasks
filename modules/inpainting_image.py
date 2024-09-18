import cv2
import numpy as np
import os

def process_images(input_folder, output_folder):
    image_files = [f for f in os.listdir(input_folder) if f.endswith(('.jpg', '.jpeg', '.png'))]

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for image_file in image_files:
        image_path = os.path.join(input_folder, image_file)
        output_path = os.path.join(output_folder, image_file)

        # Carregar a imagem
        image = cv2.imread(image_path)
        if image is None:
            print(f"Erro ao carregar a imagem: {image_path}")
            continue

        modified_image = image.copy()

        # Aqui você pode adicionar código para selecionar a região a ser removida e preenchida

        # Salvar a imagem modificada
        cv2.imwrite(output_path, modified_image)

if __name__ == "__main__":
    input_folder = input("Informe a URI da pasta de entrada das imagens: ")
    output_folder = input("Informe a URI da pasta de saída das imagens modificadas: ")

    process_images(input_folder, output_folder)

    print("Processamento de imagens concluído.")
