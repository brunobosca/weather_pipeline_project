# 🌦️ Clima em Tempo Real com Python + AWS S3

Este projeto coleta dados meteorológicos em tempo real utilizando a **API do OpenWeather**, transforma as informações em `.CSV`, e envia os dados automaticamente para um **bucket no AWS S3**, formando uma mini-pipeline de dados moderna.

---

## 🔧 Tecnologias Utilizadas

- 🐍 Python 3.10+
- ☁️ AWS S3 (armazenamento na nuvem)
- 🔐 IAM (controle de permissões seguro)
- 📦 Bibliotecas: `boto3`, `requests`, `pandas`, `python-dotenv`
- 🔄 Automação com scripts reutilizáveis

---

## 📈 Objetivo

Criar uma estrutura simples, porém escalável, de **extração de dados via API pública**, **processamento** local e **armazenamento em nuvem**, simulando o funcionamento de pipelines de dados reais em projetos profissionais.

---

## ⚙️ Como Funciona

1. **Consulta API** do OpenWeather com coordenadas definidas (lat/lon)
2. Extrai informações como:
   - Temperatura
   - Umidade
   - Condição do céu
   - Vento
3. Salva o resultado formatado em um arquivo `.csv`
4. Faz o **upload automático para o AWS S3** com segurança
5. (Opcional) Listagem de arquivos no bucket

---

## 🧪 Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/brunobosca/clima-pipeline-s3.git
cd clima-pipeline-s3

### 2. Instale os requisitos 

pip install -r requirements.txt

### 3. Configure as variáveis de ambiente

Crie um arquivo .env com as seguintes chaves:

AWS_ACCESS_KEY_ID=SUAS_CREDENCIAIS
AWS_SECRET_ACCESS_KEY=SUAS_CREDENCIAIS
AWS_REGION=us-east-2

### 4. Execute a pipeline

python pipeline.py


## 📁 Estrutura do Projeto

📦 clima-pipeline-s3
├── .env                 # Variáveis sensíveis (NÃO subir pro GitHub)
├── pipeline.py          # Pipeline principal
├── s3_upload.py         # Módulo de upload para o S3
├── listar_s3.py         # Lista arquivos no bucket
├── dados_clima.csv      # Arquivo gerado
├── README.md            # Este arquivo
└── requirements.txt     # Dependências


## 🚀 Potenciais Extensões

Armazenamento contínuo com agendamento (cron/Lambda)

Upload particionado por data (YYYY/MM/DD/arquivo.csv)

Conexão com bancos como Redshift, Athena, BigQuery, etc.

Visualização com Power BI ou Looker Studio (via S3 ou API)


## 🔒 Segurança
Este projeto segue boas práticas de segurança:

Uso de .env para variáveis sensíveis

Acesso controlado via usuário IAM com política mínima

Nunca expõe chaves diretamente no código

## 💼 Sobre Mim
👋 Me chamo Bruno e este projeto é parte do meu portfólio voltado para engenharia de dados, cloud e automação de pipelines com Python.
Estou em constante evolução e buscando oportunidades para aplicar essas habilidades em ambientes reais.

## 📲 Contato
LinkedIn: linkedin.com/in/brunoboscaini

GitHub: github.com/brunobosca


