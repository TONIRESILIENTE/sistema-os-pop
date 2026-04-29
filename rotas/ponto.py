"""
Rota: /ponto
Protegida — apenas gestores e admins.
Protected — managers and admins only.
"""

from fastapi import APIRouter, Depends
from datetime import date
from seguranca.jwt import requer_gestor

router = APIRouter(prefix="/ponto", tags=["Ponto Biométrico"])


@router.get("/hoje", dependencies=[Depends(requer_gestor)])
def ponto_hoje():
    """
    Retorna quem bateu ponto hoje.
    Returns who clocked in today.
    Requires: gestor or admin level.
    """
    hoje = date.today().strftime("%Y-%m-%d")
    return [
        {"id": 1, "nome": "Carlos Eduardo",  "hora_entrada": "07:12", "hora_saida": None, "data": hoje},
        {"id": 2, "nome": "Fernanda Lima",    "hora_entrada": "07:58", "hora_saida": None, "data": hoje},
        {"id": 3, "nome": "Roberto Alves",    "hora_entrada": "08:05", "hora_saida": None, "data": hoje},
        {"id": 4, "nome": "Juliana Santos",   "hora_entrada": "08:01", "hora_saida": None, "data": hoje},
        {"id": 5, "nome": "Marcos Pereira",   "hora_entrada": "06:55", "hora_saida": None, "data": hoje},
        {"id": 6, "nome": "Ana Paula Costa",  "hora_entrada": "07:30", "hora_saida": None, "data": hoje},
        {"id": 7, "nome": "Diego Menezes",    "hora_entrada": "07:45", "hora_saida": None, "data": hoje},
        {"id": 8, "nome": "Letícia Rocha",    "hora_entrada": "08:00", "hora_saida": None, "data": hoje},
    ]
