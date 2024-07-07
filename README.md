# Desenvolvendo FastAPI com Docker e SQLAlchemy

Este projeto é uma API desenvolvida utilizando FastAPI, Docker e SQLAlchemy. O objetivo principal é gerenciar atletas, centros de treinamento e categorias. A API permite criar, ler, atualizar e deletar registros, além de implementar paginação, customizar responses e manipular exceções de integridade dos dados.

## Funcionalidades

- **Query Parameters nos Endpoints**
  - **Atleta**:
    - Filtro por `nome`
    - Filtro por `cpf`

- **Customização de Responses**
  - **Get All Atletas**:
    - Campos: `nome`, `centro_treinamento`, `categoria`

- **Manipulação de Exceções de Integridade dos Dados**
  - Manipulação de `sqlalchemy.exc.IntegrityError`
  - Mensagem de erro: “Já existe um atleta cadastrado com o cpf: {cpf}”
  - Código de status: 303

- **Paginação com fastapi-pagination**
  - Implementação de `limit` e `offset`

## Estrutura do Projeto

```plaintext
├── .venv
├── alembic
│   ├── __pycache__
│   ├── versions
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── env
├── workout_api
│   ├── atleta
│   │   ├── __pycache__
│   │   ├── __init__.py
│   │   ├── controller.py
│   │   ├── models.py
│   │   └── schemas.py
│   ├── categorias
│   │   ├── __pycache__
│   │   ├── __init__.py
│   │   ├── controller.py
│   │   ├── models.py
│   │   └── schemas.py
│   ├── centro_treinamento
│   │   ├── __pycache__
│   │   ├── __init__.py
│   │   ├── controller.py
│   │   ├── models.py
│   │   └── schemas.py
│   ├── configs
│   ├── contrib
│   │   ├── __init__.py
│   ├── main.py
│   ├── routers.py
│   └── __project
│       └── alembic.ini
├── docker-compose.yml
├── Makefile
└── requirements.txt
