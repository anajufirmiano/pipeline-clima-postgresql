# 🌦️ Pipeline ETL: OpenWeather para PostgreSQL

Pipeline de engenharia de dados ponta a ponta (ETL) desenvolvido em ambiente Linux (WSL) utilizando Python e PostgreSQL.

## 🛠️ Arquitetura do Pipeline

* **Extract:** Extração automatizada de dados meteorológicos via API REST da OpenWeather em formato JSON.
* **Transform:** Limpeza, seleção de métricas e conversão tabular utilizando `pandas`, com geração de timestamp de coleta.
* **Load:** Carga e persistência dos dados tratados no banco relacional PostgreSQL com `SQLAlchemy` e driver `psycopg` (modo append).

## 🧰 Tecnologias

* Python
* PostgreSQL
* Pandas, Requests, SQLAlchemy, Psycopg (v3), Python-dotenv
* Linux (Ubuntu via WSL)

## 🚀 Como Executar

1. Clone o repositório:
```bash
git clone [https://github.com/anajufirmiano/pipeline-clima-postgresql.git](https://github.com/anajufirmiano/pipeline-clima-postgresql.git)
cd pipeline-clima-postgresql
