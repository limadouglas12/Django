# Django Polls Tutorial Project

Este projeto implementa o tutorial oficial do Django 6.0 at� a parte 8.

## O que est� inclu�do

- App `polls` com modelos `Question` e `Choice`
- Registro no admin do `Question` e `ChoiceInline`
- Views baseadas em classes para listagem, detalhes e resultados
- Sistema de vota��o com redirect ap�s submiss�o
- Templates para `index`, `detail` e `results`
- Testes unit�rios para modelos e views
- Arquivos est�ticos servidos a partir de `polls/static/`
- Superusu�rio criado localmente para acesso ao admin
- `requirements.txt` com depend�ncias do projeto
- `.gitignore` j� configurado para `db.sqlite3`, `venv/` e arquivos Python tempor�rios

## Estrutura de URLs

- `/` → página inicial do app `blog`
- `/polls/` → página inicial do app `polls`
- `/admin/` → admin Django

## Superusu�rio local

- Usu�rio: `admin`
- Email: `admin@example.com`
- Senha: `admin123`

> Altere a senha depois de fazer o login no admin.

## Como usar

1. Ative a virtualenv:
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```
2. Instale as depend�ncias:
   ```powershell
   pip install -r requirements.txt
   ```
3. Crie o banco de dados e aplique migra��es:
   ```powershell
   python manage.py migrate
   ```
4. Execute o servidor local:
   ```powershell
   python manage.py runserver
   ```
5. Acesse o site:
   - http://127.0.0.1:8000/ (blog)
   - http://127.0.0.1:8000/polls/ (enquetes)
   - http://127.0.0.1:8000/admin/

## Deployment (parte 8 do tutorial)

Para subir no GitHub e depois em um servidor como PythonAnywhere:

1. Crie um reposit�rio no GitHub e fa�a commit do projeto.
2. N�o inclua `db.sqlite3` nem `venv/`, pois j� est�o ignorados no `.gitignore`.
3. No servidor de deployment, crie um ambiente virtual e instale as depend�ncias:
   ```bash
   python -m venv venv
   source venv/bin/activate  # ou venv\Scripts\Activate.ps1 no Windows
   pip install -r requirements.txt
   ```
4. Configure as vari�veis de ambiente, especialmente `SECRET_KEY`.
5. Rode as migra��es:
   ```bash
   python manage.py migrate
   ```
6. Crie um superusu�rio se necess�rio:
   ```bash
   python manage.py createsuperuser
   ```
7. Execute o servidor ou configure o servi�o do servidor web.

## Observa��es

- O projeto usa `python-dotenv` para carregar `SECRET_KEY` de um arquivo `.env` quando dispon�vel.
- Para GitHub, adicione um arquivo `.env.example` com o modelo de vari�vel de ambiente.
