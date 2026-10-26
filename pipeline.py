import os
import requests
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Carrega as variáveis do arquivo .env
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

CIDADE = "Rio de Janeiro"

# 1. EXTRACT
print("1. Buscando dados na OpenWeather...")
url = f"https://api.openweathermap.org/data/2.5/weather?q={CIDADE}&appid={API_KEY}&units=metric&lang=pt_br"
resposta = requests.get(url)
resposta.raise_for_status()
dados_brutos = resposta.json()

# 2. TRANSFORM
print("2. Tratando os dados...")
dados_limpos = {
    "cidade": dados_brutos["name"],
    "temperatura": dados_brutos["main"]["temp"],
    "sensacao_termica": dados_brutos["main"]["feels_like"],
    "umidade": dados_brutos["main"]["humidity"],
    "descricao_tempo": dados_brutos["weather"][0]["description"],
    "data_hora_coleta": datetime.now()
}

df = pd.DataFrame([dados_limpos])
print("\nTabela tratada:")
print(df)

# 3. LOAD
print("\n3. Salvando no PostgreSQL...")
url_banco = f"postgresql+psycopg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
conexao = create_engine(url_banco)

df.to_sql("clima_atual", con=conexao, if_exists="append", index=False)
print("\nSucesso! Pipeline concluido e dado persistido no banco.")