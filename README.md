# PRISMA Platform — Gestão de Manutenção

Sistema de gerenciamento de ordens de serviço e procedimentos operacionais (POPs) com autenticação JWT e níveis de acesso.

## 🚀 Como executar

```bash
# 1. Criar ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Configurar variáveis de ambiente
copy .env.example .env
# Edite o arquivo .env com sua chave secreta JWT

# 4. Executar o servidor
uvicorn main:app --reload