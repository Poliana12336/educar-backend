# educAR Backend

API desenvolvida com FastAPI para gerenciamento da plataforma educacional educAR.

O backend é responsável pelo controle de usuários, turmas, capítulos, liberações de conteúdo e integração com o frontend da plataforma.

---

# Sobre o projeto

O educAR é uma plataforma educacional com Realidade Aumentada que permite a integração entre conteúdos didáticos digitais e experiências interativas utilizando AR.js.

A API gerencia os dados da aplicação e fornece os endpoints utilizados pelos dashboards e pelo livro digital.

---

# Funcionalidades

- Login de usuários
- Cadastro de usuários
- Cadastro de turmas
- Matrícula de alunos
- Gerenciamento de capítulos
- Liberação de capítulos para turmas
- Controle de acesso por roles
- API integrada ao frontend

---

# Tecnologias utilizadas

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Cloudflare Tunnel

---

# Estrutura do projeto

```text
educar-backend/
│
├── app/
│   │
│   ├── models/
│   ├── routes/
│   ├── seeds/
│   ├── create_tables.py
│   ├── database.py
│   └── main.py
│
├── requirements.txt
├── README.md
├── educar.db
└── .gitignore
```

---

# Como executar o backend

## 1. Clone o repositório

```bash
git clone LINK_BACKEND
```

---

## 2. Acesse a pasta

```bash
cd educar-backend
```

---

## 3. Crie ambiente virtual

```bash
python -m venv venv
```

---

## 4. Ative o ambiente virtual

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

---

## 5. Instale as dependências

```bash
pip install -r requirements.txt
```

---

# Instalação do Cloudflare Tunnel

O Cloudflare Tunnel será utilizado para gerar um link HTTPS público da API, permitindo integração com o frontend em dispositivos móveis.

---

## Windows

Baixe o Cloudflared:

https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/downloads/

Após baixar, coloque o executável dentro da pasta do projeto ou em uma pasta acessível pelo terminal.

---

# Como executar o backend

## 1. Execute o servidor FastAPI

```bash
uvicorn app.main:app --reload --host 0.0.0.0
```

---

## 2. Execute o Cloudflare Tunnel

```bash
./cloudflared tunnel --url http://localhost:8000
```

---

# Acesse a documentação

```text
http://127.0.0.1:8000/docs
```

---

# Link HTTPS da API

O terminal irá gerar um link semelhante a:

```text
https://xxxxx.trycloudflare.com
```

Esse será o endereço público da API.

---

# Configuração obrigatória no frontend

No frontend, abra:

```text
js/api.js
```

e altere:

```javascript
const API_URL = "http://127.0.0.1:8000";
```

para:

```javascript
const API_URL = "https://SEU-LINK-CLOUDFLARE.trycloudflare.com";
```

Exemplo:

```javascript
const API_URL = "https://abc123.trycloudflare.com";
```

---

# Banco de dados

O projeto utiliza SQLite para armazenamento dos dados da aplicação.

As tabelas principais incluem:

- users
- turmas
- aluno_turma
- capitulos
- liberacoes

---

# Roles do sistema

## Gestão

- Cadastro de usuários
- Cadastro de turmas

## Professor

- Liberação de capítulos

## Aluno

- Acesso aos capítulos liberados

---

# Objetivo

Gerenciar os dados e funcionalidades da plataforma educAR, integrando conteúdos educacionais digitais com experiências em Realidade Aumentada.

---

# Equipe

- Poliana Lima Carvalho
- Isamara Silva Evangelista
- Raylla Myrellen Sousa Morais
- Yasmim Evellyn Barbosa Ribeiro
- Raimundo Ítalo Muniz Ribeiro

---

# Orientadora

- Sabrina Nicolle Rodrigues Sousa Rosa
