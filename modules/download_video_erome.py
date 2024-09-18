import requests

# URL do vídeo
video_url = "https://v60.erome.com/1601/i7K5A07I/CPW4SUNT_720p.mp4"

# Definindo os headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Cookie": "laravel_session=eyJpdiI6IlRkNDZ1SjVJdm1Dd2JUdGpucUhIaUE9PSIsInZhbHVlIjoiMW43UGdDRVgwdnB1R2lNKytOWUczQlZtV0lKaXBqUHhJenloVzNsRHl2b3FQWk1KUGJcL3dMWmdZVkRkVGpaeVhJeTJJcUpwTnhVSGFBVzk1cFlTN1JRPT0iLCJtYWMiOiJkODA4NzZiMzQzZWVhZGNjMTczNzBkNzA5MWVhMDUzNGVmNTc2YmQxNjFjNTVhZjk2ZWZhMjE1YmIzMTgwNTFjIn0%3D"
}

# Baixando o vídeo
filename = video_url.split("/")[-1]
with requests.get(video_url, headers=headers, stream=True) as r:
    with open(filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)

print(f"Vídeo {filename} baixado com sucesso!")

