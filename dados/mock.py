"""
Dados fictícios para modo DEMO.
Mock data for DEMO mode.
"""
from datetime import datetime, timedelta


def mins_atras(m): return (datetime.now() - timedelta(minutes=m)).isoformat()


COLABORADORES_MOCK = [
    {"id": 1, "nome": "Carlos Eduardo", "cargo": "Técnico Eletricista", "status": "on", "ultima_sync": mins_atras(2), "foto": None,
     "ordens": [
         {"id": "OS-2401", "descricao": "Instalação de quadro elétrico — Bloco A", "status": "Em Execução",
             "prioridade": "Alta", "local": "Bloco A / Sala 12", "abertura": "07:30", "prazo": "12:00", "tipo": "Elétrica"},
         {"id": "OS-2402", "descricao": "Troca de disjuntores — Almoxarifado", "status": "Aberta",
             "prioridade": "Média", "local": "Almoxarifado", "abertura": "08:00", "prazo": "14:00", "tipo": "Elétrica"},
         {"id": "OS-2398", "descricao": "Revisão geral painel principal", "status": "Concluída", "prioridade": "Baixa",
             "local": "Sala Técnica", "abertura": "06:00", "prazo": "08:00", "tipo": "Preventiva"},
    ]},
    {"id": 2, "nome": "Fernanda Lima", "cargo": "Técnica de Refrigeração", "status": "offline", "ultima_sync": mins_atras(47), "foto": None,
     "ordens": [
         {"id": "OS-2405", "descricao": "Recarga de gás ar-condicionado — Diretoria", "status": "Concluída",
             "prioridade": "Alta", "local": "Diretoria / Sala 01", "abertura": "06:30", "prazo": "09:00", "tipo": "Refrigeração"},
         {"id": "OS-2407", "descricao": "Instalação split 18.000 BTUs — TI", "status": "Em Execução", "prioridade": "Alta",
             "local": "TI / Sala Servidores", "abertura": "11:30", "prazo": "17:00", "tipo": "Refrigeração"},
    ]},
    {"id": 3, "nome": "Roberto Alves", "cargo": "Encanador Hidráulica", "status": "offline", "ultima_sync": mins_atras(18), "foto": None,
     "ordens": [
         {"id": "OS-2410", "descricao": "Reparo em vazamento — Banheiro 3º Andar", "status": "Aberta", "prioridade": "Alta",
             "local": "Banheiro / 3º Andar", "abertura": "08:15", "prazo": "11:00", "tipo": "Hidráulica"},
         {"id": "OS-2411", "descricao": "Desentupimento cano esgoto — Refeitório", "status": "Aberta",
             "prioridade": "Alta", "local": "Refeitório", "abertura": "08:30", "prazo": "12:00", "tipo": "Hidráulica"},
    ]},
    {"id": 4, "nome": "Juliana Santos", "cargo": "Técnica em Edificações", "status": "on", "ultima_sync": mins_atras(5), "foto": None,
     "ordens": [
         {"id": "OS-2415", "descricao": "Vistoria estrutural — Cobertura Bloco B", "status": "Em Execução",
             "prioridade": "Alta", "local": "Bloco B / Cobertura", "abertura": "09:00", "prazo": "16:00", "tipo": "Preventiva"},
         {"id": "OS-2416", "descricao": "Pintura corredor principal", "status": "Em Execução", "prioridade": "Baixa",
             "local": "Corredor / 1º Andar", "abertura": "13:00", "prazo": "18:00", "tipo": "Conservação"},
    ]},
    {"id": 5, "nome": "Toni Muniz", "cargo": "Eletricista Industrial", "status": "on", "ultima_sync": mins_atras(1), "foto": None,
     "ordens": [
         {"id": "OS-2420", "descricao": "Cabeamento elétrico novos geradores", "status": "Concluída",
             "prioridade": "Alta", "local": "Casa de Máquinas", "abertura": "06:00", "prazo": "10:00", "tipo": "Elétrica"},
         {"id": "OS-2422", "descricao": "SPDA — Inspeção para-raios", "status": "Aberta", "prioridade": "Média",
             "local": "Telhado / Bloco Central", "abertura": "14:00", "prazo": "17:00", "tipo": "Elétrica"},
    ]},
    {"id": 6, "nome": "Ana Paula Costa", "cargo": "Supervisora de Manutenção", "status": "on", "ultima_sync": mins_atras(3), "foto": None,
     "ordens": [
         {"id": "OS-2430", "descricao": "Auditoria geral — ordens do dia", "status": "Concluída", "prioridade": "Alta",
             "local": "Escritório Manutenção", "abertura": "07:00", "prazo": "12:00", "tipo": "Gestão"},
         {"id": "OS-2431", "descricao": "Relatório mensal de equipamentos", "status": "Aberta",
             "prioridade": "Média", "local": "Escritório", "abertura": "13:00", "prazo": "17:00", "tipo": "Gestão"},
    ]},
    {"id": 7, "nome": "Diego Menezes", "cargo": "Técnico de Segurança", "status": "offline", "ultima_sync": mins_atras(92), "foto": None,
     "ordens": [
         {"id": "OS-2441", "descricao": "Teste alarme incêndio — Bloco C", "status": "Concluída",
             "prioridade": "Alta", "local": "Bloco C", "abertura": "10:00", "prazo": "13:00", "tipo": "Segurança"},
         {"id": "OS-2442", "descricao": "Calibração detectores fumaça", "status": "Aberta", "prioridade": "Média",
             "local": "Todos os andares", "abertura": "14:00", "prazo": "17:30", "tipo": "Preventiva"},
    ]},
    {"id": 8, "nome": "Letícia Rochas Augusta", "cargo": "Técnica de Automação", "status": "on", "ultima_sync": mins_atras(8), "foto": None,
     "ordens": [
         {"id": "OS-2450", "descricao": "Programação CLP linha produção A", "status": "Em Execução", "prioridade": "Alta",
             "local": "Produção / Linha A", "abertura": "08:00", "prazo": "16:00", "tipo": "Automação"},
         {"id": "OS-2451", "descricao": "Atualização firmware controladores", "status": "Aberta", "prioridade": "Média",
             "local": "Sala de Controle", "abertura": "16:30", "prazo": "18:00", "tipo": "Automação"},
    ]},
    {"id": 9, "nome": "Pedrão", "cargo": "Manutencista", "status": "on", "ultima_sync": mins_atras(8), "foto": None,
     "ordens": [
        {"id": "OS-2450", "descricao": "Programação CLP linha produção A", "status": "Em Execução", "prioridade": "Alta",
         "local": "Produção / Linha A", "abertura": "08:00", "prazo": "16:00", "tipo": "Automação"},
         {"id": "OS-2451", "descricao": "Atualização firmware controladores", "status": "Aberta", "prioridade": "Média",
             "local": "Sala de Controle", "abertura": "16:30", "prazo": "18:00", "tipo": "Automação"},
    ]},
]
