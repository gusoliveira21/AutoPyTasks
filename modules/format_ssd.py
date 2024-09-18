import psutil
import subprocess
import os

def listar_dispositivos():
    print("Listando dispositivos de armazenamento:")
    for part in psutil.disk_partitions():
        if 'cdrom' in part.opts or part.fstype == '':
            continue
        uso = psutil.disk_usage(part.mountpoint)
        print(f"Dispositivo: {part.device}, Espaço disponível: {uso.free // (2**30)}GB, Tipo: {part.fstype}")

def formatar_dispositivo(dispositivo, sistema_arquivos='exfat'):
    print(f"Formatando {dispositivo} para {sistema_arquivos}...")
    try:
        subprocess.run(['sudo', 'mkfs', f'-t {sistema_arquivos}', dispositivo], check=True)
        print(f"Dispositivo {dispositivo} formatado com sucesso.")
    except Exception as e:
        print(f"Erro ao formatar o dispositivo: {e}")

def listar_unidades_windows():
    try:
        subprocess.run("wmic logicaldisk get name, freespace, size, filesystem", shell=True)
    except Exception as e:
        print(f"Erro ao listar unidades: {e}")

def formatar_unidade_windows(unidade, sistema_arquivos='exfat'):
    try:
        script_diskpart = f"""
        select volume {unidade}
        format fs={sistema_arquivos} quick
        """
        subprocess.run(['diskpart'], input=script_diskpart, text=True, check=True)
        print(f"Unidade {unidade} formatada com sucesso para {sistema_arquivos}.")
    except Exception as e:
        print(f"Erro ao formatar a unidade: {e}")

if __name__ == "__main__":
    #listar_dispositivos()
    #listar_unidades_windows()
    listar_unidades_windows()
    unidade = input("Digite a letra da unidade para formatar (ex: D): ").strip()
    confirmacao = input(f"Tem certeza que deseja formatar {unidade}? Isso irá apagar todos os dados na unidade. (s/n): ").lower()
    if confirmacao == 's':
        formatar_unidade_windows(unidade)
    else:
        print("Operação cancelada.")
