"""
╔══════════════════════════════════════════════════════╗
║         PRISMA Platform — Back-end API               ║
║         Com autenticação JWT e níveis de acesso      ║
║         With JWT authentication and access levels    ║
╚══════════════════════════════════════════════════════╝

COMO RODAR / HOW TO RUN:
  pip install -r requirements.txt
  python -m uvicorn main:app --reload

ACESSOS / ACCESS:
  Dashboard:  http://localhost:8000/dashboard
  POP Mobile: http://localhost:8000/pop
  API Docs:   http://localhost:8000/docs

USUÁRIOS DE TESTE / TEST USERS:
  admin    / admin123    → acesso total
  anapaula / gestor123  → gestor
  carlos   / carlos123  → colaborador
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from datetime import datetime
import os

from rotas import auth, colaboradores, ordens, ponto

app = FastAPI(
    title="PRISMA Platform API",
    description="""
    ## API da Plataforma de Manutenção PRISMA

    ### Autenticação / Authentication
    1. Faça POST em `/auth/login` com username e password
    2. Copie o `access_token` retornado
    3. Clique em **Authorize** (cadeado) e cole: `Bearer <seu_token>`
    4. Agora pode usar todas as rotas protegidas

    ### Níveis de Acesso / Access Levels
    - **admin** → acesso total a tudo
    - **gestor** → vê todos os colaboradores e OS
    - **colaborador** → vê apenas seus próprios dados
    """,
    version="2.0.0"
)

# ── CORS ──────────────────────────────────────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # Em produção: especifique os IPs permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Rotas / Routes ────────────────────────────────────────────────────────────
app.include_router(auth.router)
app.include_router(colaboradores.router)
app.include_router(ordens.router)
app.include_router(ponto.router)

# ── Servir páginas HTML / Serve HTML pages ────────────────────────────────────
@app.get("/dashboard", tags=["Páginas"])
def abrir_dashboard():
    """Dashboard principal — TV / Gestor"""
    caminho = "dashboard-prisma-com-fotos.html"
    if os.path.exists(caminho):
        return FileResponse(caminho, media_type="text/html")
    return {"erro": f"Coloque '{caminho}' na pasta do projeto"}

@app.get("/pop", tags=["Páginas"])
def abrir_pop():
    """POP Mobile — Colaborador no Campo"""
    caminho = "prisma-pop.html"
    if os.path.exists(caminho):
        return FileResponse(caminho, media_type="text/html")
    return {"erro": f"Coloque '{caminho}' na pasta do projeto"}

# ── Status ────────────────────────────────────────────────────────────────────
@app.get("/", tags=["Status"])
def raiz():
    return {
        "status":  "online",
        "sistema": "PRISMA Platform API",
        "versao":  "2.0.0",
        "hora":    datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "seguranca": "JWT Authentication ativo",
        "paginas": {
            "dashboard":  "http://localhost:8000/dashboard",
            "pop_mobile": "http://localhost:8000/pop",
            "api_docs":   "http://localhost:8000/docs",
        },
        "usuarios_teste": {
            "admin":    "admin123   → acesso total",
            "gestor":   "gestor123  → anapaula",
            "colaborador": "carlos123 → carlos",
        }
    }

@app.get("/health", tags=["Status"])
def health_check():
    return {"ok": True, "timestamp": datetime.now().isoformat()}

print("")
print("🚀 PRISMA Platform API — v2.0 com Segurança JWT!")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("📊 Dashboard:  http://localhost:8000/dashboard")
print("📖 POP Mobile: http://localhost:8000/pop")
print("📚 API Docs:   http://localhost:8000/docs")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("🔐 Usuários de teste:")
print("   admin    / admin123")
print("   anapaula / gestor123")
print("   carlos   / carlos123")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("")
