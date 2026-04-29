"""
Rota: /colaboradores
Protegida por autenticação JWT e nível de acesso.
Protected by JWT authentication and access level.

Níveis de acesso / Access levels:
  - gestor/admin → vê TODOS os colaboradores
  - colaborador  → vê apenas seus próprios dados
"""

from fastapi import APIRouter, Depends, HTTPException
from seguranca.jwt import get_usuario_atual, requer_gestor
from dados.mock import COLABORADORES_MOCK

router = APIRouter(prefix="/colaboradores", tags=["Colaboradores"])


@router.get("/dia")
def colaboradores_do_dia(usuario: dict = Depends(get_usuario_atual)):
    """
    Retorna colaboradores do dia.
    Returns today's collaborators.

    - Gestor/Admin → retorna todos
    - Colaborador  → retorna apenas os próprios dados
    """
    # Gestor e admin veem todos / Managers and admins see everyone
    if usuario["nivel"] in ["gestor", "admin"]:
        return COLABORADORES_MOCK

    # Colaborador vê apenas seus próprios dados / Worker sees only own data
    meus_dados = [c for c in COLABORADORES_MOCK if c["id"] == usuario["id"]]
    if not meus_dados:
        return []
    return meus_dados


@router.get("/todos", dependencies=[Depends(requer_gestor)])
def todos_colaboradores():
    """
    Retorna TODOS os colaboradores — apenas gestores e admins.
    Returns ALL collaborators — managers and admins only.
    """
    return COLABORADORES_MOCK


@router.get("/{colaborador_id}")
def colaborador_por_id(colaborador_id: int, usuario: dict = Depends(get_usuario_atual)):
    """
    Retorna um colaborador específico.
    Returns a specific collaborator.

    - Gestor/Admin → pode ver qualquer colaborador
    - Colaborador  → só pode ver a si mesmo
    """
    # Colaborador tentando ver outro colaborador / Worker trying to see another worker
    if usuario["nivel"] == "colaborador" and usuario["id"] != colaborador_id:
        raise HTTPException(
            status_code=403,
            detail="Acesso negado — você só pode ver seus próprios dados / Access denied — you can only see your own data"
        )

    colab = next((c for c in COLABORADORES_MOCK if c["id"] == colaborador_id), None)
    if not colab:
        raise HTTPException(status_code=404, detail=f"Colaborador {colaborador_id} não encontrado")
    return colab
