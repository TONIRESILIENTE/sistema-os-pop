🛠️ Platform — Gestão de Manutenção

![Python](https://img.shields.io/badge/Python-3.13-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-green)
![JWT](https://img.shields.io/badge/JWT-autenticação-orange)
![Status](https://img.shields.io/badge/status-em_desenvolvimento-yellow)

> **Sistema web para gerenciamento de ordens de serviço e procedimentos operacionais padrão (POPs), com autenticação JWT, níveis de acesso e interfaces adaptadas para desktop e mobile.**

---

## 🎯 Objetivo

Oferecer uma plataforma centralizada onde equipes de manutenção industrial possam:

- Criar, acompanhar e encerrar **ordens de serviço (OS)**.
- Consultar **procedimentos operacionais padrão (POPs)** de forma rápida.
- Acessar o sistema de qualquer dispositivo (desktop, tablet, celular).
- Garantir segurança com **autenticação JWT** e controle de permissões por perfil de usuário.

---

## 🧠 Contexto do autor

Este projeto integra meu **portfólio de transição de carreira** da manutenção industrial para a área de tecnologia. A ideia nasceu da vivência real em fábricas, onde a falta de um sistema simples e acessível para registrar e consultar ordens de serviço ainda é uma dor constante.

Cada decisão — da escolha do framework à modelagem das rotas — foi pensada para unir **conhecimento prático de chão de fábrica** com **boas práticas de desenvolvimento de software**.

---

## 🏗️ Arquitetura do sistema




[ Navegador (desktop / mobile) ]
│
▼
[ FastAPI (backend Python) ]
│
├── Rotas protegidas por JWT
├── Templates HTML (Jinja2)
└── Banco de dados (a definir)



### Principais módulos

- **Autenticação**: login com JWT, proteção de rotas, expiração de token.
- **Ordens de serviço**: criação, listagem, edição e encerramento.
- **POPs**: consulta a procedimentos técnicos cadastrados.
- **Dashboard**: visão geral para desktop e versão adaptada para mobile.

---

## 🛠️ Stack tecnológica

| Ferramenta | Função |
|------------|--------|
| **Python 3.13** | Linguagem principal |
| **FastAPI** | Framework web (backend) |
| **Jinja2** | Templates HTML |
| **JWT (JSON Web Token)** | Autenticação stateless |
| **HTML5 + CSS3** | Interfaces responsivas |
| **Uvicorn** | Servidor ASGI |
| **Git & GitHub** | Versionamento e portfólio |

---

## 📁 Estrutura do projeto
sistema-os-pop/
├── main.py # Aplicação FastAPI
├── config.py # Configurações (JWT, etc.)
├── requirements.txt # Dependências
├── .env.example # Exemplo de variáveis de ambiente
│
├── rotas/ # Endpoints da API
├── dados/ # Simulação de banco (JSON/CSV)
├── seguranca/ # Lógica de autenticação/autorização
│
├── dashboard-de-os.html # Interface desktop
├── mobile-de-os-pop.html # Interface mobile
│
└── README.md



---

## ⚙️ Como executar localmente

### 1. Clone o repositório

git clone https://github.com/TONIRESILIENTE/sistema-os-pop.git
cd sistema-os-pop
2. Crie e ative o ambiente virtual

python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
3. Instale as dependências

pip install -r requirements.txt
4. Configure as variáveis de ambiente

copy .env.example .env
Abra o arquivo .env e defina uma chave secreta forte para o JWT:


SECRET_KEY=sua-chave-super-secreta-aqui
5. Execute o servidor

uvicorn main:app --reload
Acesse no navegador:

Desktop: http://127.0.0.1:8000/dashboard

Mobile: http://127.0.0.1:8000/mobile

🔐 Funcionalidades implementadas
Cadastro e login com JWT

Proteção de rotas (usuário não autenticado é redirecionado)

Criação, listagem, edição e encerramento de OS

Consulta a POPs cadastrados

Interface responsiva (desktop + mobile)

Integração com banco de dados real (SQLite/PostgreSQL)

Upload de fotos nas OS (ex: foto do defeito)

Notificações por e-mail

🚧 Dificuldades enfrentadas
Dificuldade	Solução
Gerenciamento de sessão sem estado	Implementação de JWT com expiração configurável
Adaptar a interface para uso mobile em fábrica	Template separado com CSS otimizado para touch e telas pequenas
Simular banco de dados sem dependência externa	Uso de arquivos JSON/CSV na pasta dados/ (preparado para migração futura)
💡 Aprendizados
Estruturar uma API REST com FastAPI de forma modular (rotas, segurança, configurações separadas).

Implementar autenticação JWT do zero, entendendo token, payload e renovação.

Criar templates Jinja2 reutilizáveis e interfaces adaptativas.

Versionar um projeto com Git pensando em evolução contínua.

🔮 Próximos passos
Conectar a um banco de dados real (SQLite via SQLAlchemy).

Implementar upload de imagens nas ordens de serviço.

Criar painel de administração para gestão de usuários.

Containerizar com Docker para deploy simplificado.

📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

Desenvolvido por Toni Almeida Muniz como parte de uma jornada de transição de carreira. Feedbacks e contribuições são bem-vindos!