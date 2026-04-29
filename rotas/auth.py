"""
Rotas de autenticação / Authentication routes.

POST /auth/login  → faz login, retorna JWT token
GET  /auth/me     → retorna dados do usuário logado
POST /auth/logout → invalida o token (client-side)
"""

from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from datetime import datetime

from seguranca.usuarios import autenticar_usuario
from seguranca.jwt import criar_token, get_usuario_atual

router = APIRouter(prefix="/auth", tags=["Autenticação / Authentication"])


@router.post("/login")
def login(form: OAuth2PasswordRequestForm = Depends()):
    """
    Faz login e retorna o JWT token de acesso.
    Login and returns the JWT access token.

    Corpo da requisição / Request body:
      username: nome de usuário
      password: senha

    Retorno / Returns:
      access_token: JWT token para usar nas próximas requisições
      token_type: "bearer"
      nivel: nível de acesso do usuário
    """
    # Autentica o usuário / Authenticate the user
    usuario = autenticar_usuario(form.username, form.password)

    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário ou senha incorretos / Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Cria o token JWT / Create the JWT token
    token = criar_token({
        "sub":   usuario["username"],   # subject — identificador
        "nome":  usuario["nome"],
        "nivel": usuario["nivel"],      # admin | gestor | colaborador
        "id":    usuario["id"],
    })

    return {
        "access_token": token,
        "token_type":   "bearer",
        "nome":         usuario["nome"],
        "nivel":        usuario["nivel"],
        "id":           usuario["id"],
        "mensagem":     f"Bem-vindo, {usuario['nome']}! / Welcome, {usuario['nome']}!"
    }


@router.get("/me")
def meu_perfil(usuario: dict = Depends(get_usuario_atual)):
    """
    Retorna os dados do usuário autenticado.
    Returns the authenticated user's data.
    Requires: valid JWT token in Authorization header.
    """
    return {
        "id":       usuario["id"],
        "username": usuario["username"],
        "nome":     usuario["nome"],
        "email":    usuario["email"],
        "nivel":    usuario["nivel"],
        "ativo":    usuario["ativo"],
    }


@router.post("/logout")
def logout(usuario: dict = Depends(get_usuario_atual)):
    """
    Logout — no servidor o token JWT é stateless (sem estado).
    O cliente deve deletar o token localmente.
    The client should delete the token from localStorage.
    """
    return {
        "mensagem": f"Logout realizado com sucesso, {usuario['nome']}!",
        "instrucao": "Delete o token do localStorage do navegador / Delete the token from browser localStorage"
    }
