# github-actions-devops-pipeline

![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)

Pipeline CI/CD com GitHub Actions para build, testes, Docker e práticas DevOps.

## Objetivo

Construir um exemplo didático de pipeline DevOps usando GitHub Actions, com etapas progressivas para validação, build, empacotamento e publicação de uma aplicação.

Este repositório será usado para praticar automação, organização de workflows, segurança básica de pipeline e documentação de execução.

## Aplicação de exemplo

A aplicação é uma API FastAPI mínima com dois endpoints:

- `GET /`: retorna nome do serviço e status.
- `GET /health`: endpoint de healthcheck.

## O que este laboratório cobre

- Estrutura inicial de workflow no GitHub Actions.
- Etapas de lint, testes e build.
- Build de imagem Docker.
- Uso de cache e variáveis de ambiente.
- Separação de jobs por responsabilidade.
- Boas práticas de leitura de logs e troubleshooting de pipelines.
- Testes automatizados com `pytest`.
- Lint com `ruff`.

## Roadmap

- [x] Definir aplicação simples de exemplo para o pipeline.
- [x] Criar workflow inicial de CI.
- [x] Adicionar etapa de testes automatizados.
- [x] Adicionar build de imagem Docker.
- [x] Documentar fluxo de execução e falhas comuns.
- [ ] Adicionar scan básico ou validação de segurança.
- [ ] Publicar imagem em registry de laboratório.

## Como usar

Instalar dependências:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
```

No PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
```

Executar a API:

```bash
uvicorn app.main:app --reload
```

Rodar validações:

```bash
ruff check app tests
pytest
docker build -t github-actions-devops-pipeline:local .
```

## Troubleshooting de pipeline

- Falha no lint: leia a saída do `ruff` e corrija o arquivo indicado.
- Falha nos testes: rode `pytest -vv` localmente para ver o teste quebrado.
- Falha no Docker build: confira se `requirements.txt` e `Dockerfile` estão sincronizados.

## Status

Laboratório inicial implementado com app, testes, Dockerfile e workflow de CI.
