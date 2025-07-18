import pandas as pd
import json
from datetime import datetime, timezone
import os
from dotenv import load_dotenv
import requests

load_dotenv()

# URL DA API PUXANDO DO .ENV
URL = "API_KEY"

params = {
    "lat": -10,
    "lon": -55,
    "appid": os.getenv("API_KEY"),  
    "units": "metric" 
}

response = requests.get(URL, params=params)
data = response.json()

# Cria um dicionário com os campos que eu quero
registro = {
    "cidade": data["name"],
    "pais": data["sys"]["country"],
    "temperatura": data["main"]["temp"],
    "sensacao_termica": data["main"]["feels_like"],
    "umidade": data["main"]["humidity"],
    "velocidade_vento": data["wind"]["speed"],
    "data_hora": datetime.fromtimestamp(data["dt"], tz=timezone.utc)
}

# Cria DataFrame com uma linha de acordo com dict
df = pd.DataFrame([registro])

print(df)

# Salva o resultado bruto e o CSV
now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
with open(f"raw_data_{now}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

df.to_csv(f"dados_clima_{now}.csv", index=False)
