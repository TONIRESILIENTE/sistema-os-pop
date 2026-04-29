"""
Rota: /ordens
Protegida por autenticação JWT.
Protected by JWT authentication.
"""

from fastapi import APIRouter, Depends, Query
from typing import Optional
from seguranca.jwt import get_usuario_atual, requer_gestor
from dados.mock import COLABORADORES_MOCK

router = APIRouter(prefix="/ordens", tags=["Ordens de Serviço"])


@router.get("/")
def listar_ordens(
    colaborador_id: Optional[int] = Query(None),
    status: Optional[str] = Query(None),
    usuario: dict = Depends(get_usuario_atual)
):
    """
    Lista OS do dia com filtros opcionais.
    Lists work orders with optional filters.

    - Gestor/Admin → vê todas as OS
    - Colaborador  → vê apenas suas OS
    """
    todas = []
    for c in COLABORADORES_MOCK:
        # Colaborador só vê suas próprias OS / Worker only sees own orders
        if usuario["nivel"] == "colaborador" and c["id"] != usuario["id"]:
            continue
        if colaborador_id and c["id"] != colaborador_id:
            continue
        for os in c["ordens"]:
            if status and os["status"] != status:
                continue
            todas.append({**os, "colaborador_id": c["id"], "colaborador": c["nome"]})
    return todas


@router.get("/resumo", dependencies=[Depends(requer_gestor)])
def resumo_do_dia():
    """
    KPIs do dia — apenas gestores e admins.
    Day KPIs — managers and admins only.
    """
    todas = [os for c in COLABORADORES_MOCK for os in c["ordens"]]
    return {
        "total":       len(todas),
        "abertas":     len([o for o in todas if o["status"] == "Aberta"]),
        "em_execucao": len([o for o in todas if o["status"] == "Em Execução"]),
        "concluidas":  len([o for o in todas if o["status"] == "Concluída"]),
    }


@router.get("/minhas")
def minhas_ordens(usuario: dict = Depends(get_usuario_atual)):
    """
    Retorna apenas as OS do colaborador logado.
    Returns only the logged-in worker's work orders.
    """
    meu_registro = next((c for c in COLABORADORES_MOCK if c["id"] == usuario["id"]), None)
    if not meu_registro:
        return []
    return meu_registro["ordens"]
