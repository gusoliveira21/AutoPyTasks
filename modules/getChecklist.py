import asyncio
import aiohttp
import json
from aiohttp import BasicAuth

# Função para fazer uma única requisição e salvar a resposta
async def fetch_and_save(session, url, filename):
    try:
        async with session.get(url, auth=BasicAuth('gustavo.oliveira@alabia.com.br', 'alabia@123')) as response:
            content = await response.text()
            # Define um prefixo padrão para o nome do arquivo
            prefix = ""
            try:
                data = json.loads(content)
                if "message" in data:
                    prefix = "erro_"
                elif "id" in data:
                    prefix = "task_"
                if data.get("status") != 401:
                    prefix = f"not401_{prefix}"
            except json.JSONDecodeError:
                # Se não for um JSON, procede normalmente
                pass

            # Atualiza o nome do arquivo com o prefixo apropriado
            filename = f"{prefix}{filename}.txt"
            with open(filename, "w", encoding="utf-8") as file:
                file.write(content)
            print(f"Conteúdo salvo em {filename}")
    except Exception as e:
        print(f"Erro ao requisitar {url}: {e}")

# Função principal que controla as requisições assíncronas
async def main(base_url, start, end):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(start, end + 1):
            full_url = f"{base_url}{i}"
            tasks.append(fetch_and_save(session, full_url, str(i)))
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    # Solicita os dados ao usuário
    base_url = input("Digite o link base (sem o número final): ")
    start = int(input("Digite o valor inicial: "))
    end = int(input("Digite o valor final: "))
    
    # Executa o loop assíncrono
    asyncio.run(main(base_url, start, end))
