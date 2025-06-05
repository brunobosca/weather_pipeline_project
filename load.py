import boto3
import os
from dotenv import load_dotenv
from datetime import datetime
# Carrega variáveis do .env
load_dotenv()

# Credenciais e bucket
aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
region = os.getenv("AWS_REGION")
bucket_name = os.getenv("S3_BUCKET")

# Inicializa o cliente S3
s3 = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region
)

agora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Caminho do arquivo local e nome no bucket
local_path = f"data/processed/clima_tratado.csv"  # Substitua pelo caminho real
s3_key = "weather_data.csv"            # Nome do arquivo no S3

# Upload
try:
    s3.upload_file(local_path, bucket_name, s3_key)
    print(f"✅ Arquivo enviado para S3 com sucesso: s3://{bucket_name}/{s3_key}")
except Exception as e:
    print(f"❌ Erro ao enviar para o S3: {e}")
