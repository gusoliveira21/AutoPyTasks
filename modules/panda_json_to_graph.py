import json
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd

# Carragar o arquivo JSON 
file_path = r"C:\Users\Alabia\Downloads\data.json"
with open(file_path, 'r') as file:
    data = json.load(file)

# Extrair os tempos de início e término de cada tarefa    
start_times = [datetime.fromtimestamp(task['data']['startTime']) for task in data]
end_times = [datetime.fromtimestamp(task['data']['endTime']) for task in data]

# Criando um DataFrame
df = pd.DataFrame({'Start': start_times, 'End': end_times})

# Calculando a duração de cada tarefa em horas
df['Duration'] = (df['End'] - df['Start']).dt.total_seconds() / 60

# Agrupando os dados por dia e somando as durações
df['Date'] = df['Start'].dt.date
grouped_data = df.groupby('Date')['Duration'].sum()

# Plotando os dados
plt.figure(figsize=(10, 6))
grouped_data.plot(kind='line', marker='o')
plt.xlabel('Data')
plt.ylabel('Tempo Total das Tarefas (horas)')
plt.title('Tempo Total Gasto em Tarefas por Dia')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()