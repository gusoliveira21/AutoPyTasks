import aiohttp
import asyncio
import base64
from pathlib import Path

# Variáveis para contagem de sucessos e falhas
success_count = 0
error_count = 0
total_tasks = 6000

# Lock para sincronização
lock = asyncio.Lock()

async def fetch_task(session, task_id):
    global success_count, error_count
    url = f"https://api.alabiabot.com/onevoice/hw/checklist/taskId/{task_id}"
    headers = {
        "Authorization": "Basic " + base64.b64encode("gustavo.oliveira@alabia.com.br:alabia@123".encode()).decode()
    }
    
    async with session.get(url, headers=headers) as response:
        json_response = await response.json()
        if json_response.get("status") != 404:
            # Incrementando o contador de sucessos
            async with lock:
                success_count += 1
            Path(f"{task_id}.txt").write_text(str(json_response))
        else:
            # Incrementando o contador de falhas
            async with lock:
                error_count += 1

        # Calculando e exibindo a porcentagem do progresso
        async with lock:
            progress = ((task_id) / total_tasks) * 100
            print(f"Progresso: {progress:.2f}%, Sucessos: {success_count}, Falhas: {error_count}", end='\r')

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_task(session, task_id) for task_id in range(1, total_tasks + 1)]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
