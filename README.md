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
git clone https://github.com/brunosempai/clima-pipeline-s3.git
cd clima-pipeline-s3


