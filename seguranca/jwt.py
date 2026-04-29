"""
JWT — JSON Web Token
Geração e validação de tokens de autenticação.
Token generation and validation.

Como funciona / How it works:
  1. Usuário faz login com username + senha
  2. Servidor valida e gera um JWT token assinado
  3. Cliente envia o token em toda requisição no header:
     Authorization: Bearer <token>
  4. Servidor valida o token e libera o acesso
"""

from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer

from config import JWT_SECRET_KEY, JWT_ALGORITHM, JWT_EXPIRE_MINUTES
from seguranca.usuarios import buscar_usuario

# Esquema OAuth2 — define onde o token vem na requisição
# OAuth2 scheme — defines where the token comes from in the request
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def criar_token(dados: dict) -> str:
    """
    Cria um JWT token assinado.
    Creates a signed JWT token.

    O token expira após JWT_EXPIRE_MINUTES minutos.
    Token expires after JWT_EXPIRE_MINUTES minutes.
    """
    payload = dados.copy()
    expiracao = datetime.now(timezone.utc) + timedelta(minutes=JWT_EXPIRE_MINUTES)
    payload.update({
        "exp": expiracao,    # expiration time
        "iat": datetime.now(timezone.utc),  # issued at
    })
    token = jwt.encode(payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
    return token


def decodificar_token(token: str) -> dict:
    """
    Decodifica e valida um JWT token.
    Decodes and validates a JWT token.
    """
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido ou expirado / Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )


# ── Dependencies (Dependências FastAPI) ───────────────────────────────────────
# Essas funções são usadas como dependências nas rotas para protegê-las.
# These functions are used as dependencies in routes to protect them.

def get_usuario_atual(token: str = Depends(oauth2_scheme)) -> dict:
    """
    Dependency: qualquer usuário autenticado.
    Dependency: any authenticated user.
    """
    payload = decodificar_token(token)
    username = payload.get("sub")  # subject — identificador do usuário
    if not username:
        raise HTTPException(status_code=401, detail="Token inválido")
    usuario = buscar_usuario(username)
    if not usuario or not usuario["ativo"]:
        raise HTTPException(status_code=401, detail="Usuário não encontrado ou inativo")
    return usuario


def requer_gestor(usuario: dict = Depends(get_usuario_atual)) -> dict:
    """
    Dependency: apenas gestores e admins.
    Dependency: only managers and admins.
    """
    if usuario["nivel"] not in ["gestor", "admin"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Acesso negado — necessário nível gestor ou admin / Access denied — manager or admin required"
        )
    return usuario


def requer_admin(usuario: dict = Depends(get_usuario_atual)) -> dict:
    """
    Dependency: apenas admins.
    Dependency: only admins.
    """
    if usuario["nivel"] != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Acesso negado — necessário nível admin / Access denied — admin required"
        )
    return usuario
