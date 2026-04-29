"""
Configurações globais — lidas do arquivo .env
Global settings — loaded from .env file
"""
import os
from dotenv import load_dotenv

load_dotenv()

# Operação / Operation
MODO         = os.getenv("MODO", "demo")

# JWT — Autenticação / Authentication
JWT_SECRET_KEY     = os.getenv("JWT_SECRET_KEY", "chave-insegura-troque-em-producao")
JWT_ALGORITHM      = os.getenv("JWT_ALGORITHM", "HS256")
JWT_EXPIRE_MINUTES = int(os.getenv("JWT_EXPIRE_MINUTES", 480))

# PRISMA API
PRISMA_URL   = os.getenv("PRISMA_URL", "")
PRISMA_TOKEN = os.getenv("PRISMA_TOKEN", "")

# Banco de dados / Database
DB_TIPO    = os.getenv("DB_TIPO", "sqlserver")
DB_HOST    = os.getenv("DB_HOST", "localhost")
DB_PORTA   = os.getenv("DB_PORTA", "1433")
DB_NOME    = os.getenv("DB_NOME", "")
DB_USUARIO = os.getenv("DB_USUARIO", "")
DB_SENHA   = os.getenv("DB_SENHA", "")

# Geral
API_PORTA  = int(os.getenv("API_PORTA", 8000))
