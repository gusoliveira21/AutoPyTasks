import cv2
import os

def extract():
    video_uri = input("Informe a URI do vídeo: ")
    output_directory = input("Informe a URI da pasta de saída para os quadros: ")

    cap = cv2.VideoCapture(video_uri)

    if not cap.isOpened():
        print("Erro ao abrir o vídeo.")
        return 0

    video_name = os.path.splitext(os.path.basename(video_uri))[0]

    os.makedirs(output_directory, exist_ok=True)

    frame_count = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        frame_filename = os.path.join(output_directory, f'{video_name}_frame_{frame_count:04d}.jpg')
        cv2.imwrite(frame_filename, frame)
        frame_count += 1

        cv2.waitKey(10)

    cap.release()

    return frame_count

if __name__ == "__main__":
    extracted_frames = extract()

    if extracted_frames > 0:
        print(f"Foram extraídas {extracted_frames} imagens do vídeo e salvas na pasta de saída.")
    else:
        print("Nenhuma imagem foi extraída.")
