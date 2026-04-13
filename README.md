# Jornal Online - Projeto Django

Este é um projeto simples de um jornal online desenvolvido em Django para fins de avaliação.

## Requisitos
- Python 3.x
- Django 5.x

## Funcionalidades
- **Listagem de Artigos:** Uma página inicial que lista os títulos de todas as notícias publicadas.
- **Visualização de Artigo:** Página detalhada que mostra o título, corpo do texto e data de publicação de um artigo.
- **Sistema de Comentários:** Página dedicada para visualizar comentários de um artigo e publicar novos comentários.

## Como Executar
1. Instale o Django: `pip install django`
2. Aplique as migrações: `python manage.py migrate`
3. Inicie o servidor: `python manage.py runserver`
4. Aceda ao site em: `http://127.0.0.1:8000/`

## Administração
Para aceder à área de administração (`/admin`), crie um superutilizador:
`python manage.py createsuperuser`
