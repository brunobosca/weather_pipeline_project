# transform.py

import pandas as pd
import os
from datetime import datetime

# 1. Códigos para ler o CSV mais recente salvo dentro da pasta raw
raw_path = "data/raw"
arquivos = sorted(os.listdir(raw_path), reverse=True)
arquivo_csv = [a for a in arquivos if a.endswith(".csv")][0]

df = pd.read_csv(os.path.join(raw_path, arquivo_csv))

# 2. Ver o conteúdo
print("Dados brutos: ")
print(df.head())

# 3. Converter coluna de data (se ainda não estiver em datetime)
df['data_hora'] = pd.to_datetime(df['data_hora'])

# Verificação se tipo de coluna foi alterado
print(df.info())

# Colunas derivadas, Ex: temp em Fahrenheit 
df['temperatura_fahrenheit'] = df['temperatura'] * 9/5 + 32

print(df.head())
#Variável para arquivo processado
processed_path = "data/processed"

#Direcionar para onde salvar o arquivo
os.makedirs(processed_path, exist_ok=True)

#Configurando nome do arquivo a ser processado
agora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

#Salvando arquivo com os parâmetros passados
df.to_csv(os.path.join(processed_path, f"clima_tratado.csv"), index=False)

print("Transformação concluída com sucesso!")