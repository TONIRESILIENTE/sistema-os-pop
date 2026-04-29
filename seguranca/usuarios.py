"""
Gerenciamento de usuários e senhas.
User management and password handling.

Em produção, esses usuários virão do banco de dados.
In production, users will come from the database.

Níveis de acesso / Access levels:
  - admin      → acesso total / full access
  - gestor     → vê todos os colaboradores / sees all collaborators  
  - colaborador → vê apenas suas próprias OS / sees only own work orders
"""

from passlib.context import CryptContext

# Contexto de criptografia — usa bcrypt (padrão da indústria)
# Cryptography context — uses bcrypt (industry standard)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_senha(senha: str) -> str:
    """Cria hash seguro da senha / Creates secure password hash"""
    return pwd_context.hash(senha)


def verificar_senha(senha: str, hash: str) -> bool:
    """Verifica se a senha está correta / Verifies if password is correct"""
    return pwd_context.verify(senha, hash)


# ── Base de usuários / Users database ────────────────────────────────────────
# ⚠ Em produção: buscar do banco de dados, não ficar hardcoded aqui!
# ⚠ In production: fetch from database, don't hardcode here!
#
# Para gerar hash de uma nova senha no terminal:
# python -c "from passlib.context import CryptContext; c=CryptContext(schemes=['bcrypt']); print(c.hash('minhasenha'))"

USUARIOS_DB = {
    # ── Admin ──────────────────────────────────────────
    "admin": {
        "id":       0,
        "username": "admin",
        "nome":     "Administrador",
        "email":    "admin@empresa.com",
        "nivel":    "admin",          # admin | gestor | colaborador
        "ativo":    True,
        # Senha: admin123 (troque em produção!)
        "senha_hash": hash_senha("admin123"),
    },

    # ── Gestores / Managers ────────────────────────────
    "anapaula": {
        "id":       6,
        "username": "anapaula",
        "nome":     "Ana Paula Costa",
        "email":    "anapaula@empresa.com",
        "nivel":    "gestor",
        "ativo":    True,
        # Senha: gestor123 (troque em produção!)
        "senha_hash": hash_senha("gestor123"),
    },

    # ── Colaboradores / Workers ────────────────────────
    "carlos": {
        "id":       1,
        "username": "carlos",
        "nome":     "Carlos Eduardo",
        "email":    "carlos@empresa.com",
        "nivel":    "colaborador",
        "ativo":    True,
        # Senha: carlos123 (troque em produção!)
        "senha_hash": hash_senha("carlos123"),
    },
    "fernanda": {
        "id":       2,
        "username": "fernanda",
        "nome":     "Fernanda Lima",
        "email":    "fernanda@empresa.com",
        "nivel":    "colaborador",
        "ativo":    True,
        "senha_hash": hash_senha("fernanda123"),
    },
    "roberto": {
        "id":       3,
        "username": "roberto",
        "nome":     "Roberto Alves",
        "email":    "roberto@empresa.com",
        "nivel":    "colaborador",
        "ativo":    True,
        "senha_hash": hash_senha("roberto123"),
    },
    "juliana": {
        "id":       4,
        "username": "juliana",
        "nome":     "Juliana Santos",
        "email":    "juliana@empresa.com",
        "nivel":    "colaborador",
        "ativo":    True,
        "senha_hash": hash_senha("juliana123"),
    },
    "marcos": {
        "id":       5,
        "username": "marcos",
        "nome":     "Marcos Pereira",
        "email":    "marcos@empresa.com",
        "nivel":    "colaborador",
        "ativo":    True,
        "senha_hash": hash_senha("marcos123"),
    },
    "diego": {
        "id":       7,
        "username": "diego",
        "nome":     "Diego Menezes",
        "email":    "diego@empresa.com",
        "nivel":    "colaborador",
        "ativo":    True,
        "senha_hash": hash_senha("diego123"),
    },
    "leticia": {
        "id":       8,
        "username": "leticia",
        "nome":     "Letícia Rocha",
        "email":    "leticia@empresa.com",
        "nivel":    "colaborador",
        "ativo":    True,
        "senha_hash": hash_senha("leticia123"),
    },
}


def buscar_usuario(username: str) -> dict | None:
    """Busca usuário pelo username / Find user by username"""
    return USUARIOS_DB.get(username)


def autenticar_usuario(username: str, senha: str) -> dict | None:
    """
    Autentica usuário — verifica username e senha.
    Authenticate user — checks username and password.
    Returns user dict if valid, None if invalid.
    """
    usuario = buscar_usuario(username)
    if not usuario:
        return None
    if not usuario["ativo"]:
        return None
    if not verificar_senha(senha, usuario["senha_hash"]):
        return None
    return usuario
