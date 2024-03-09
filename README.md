# aplicativo para gestão de tarefas

Esta é uma aplicação web de lista de tarefas desenvolvida em Python usando o framework Flask.

## Funcionalidades

- Adicionar uma nova tarefa.
- Excluir tarefas existentes.
- Visualizar a lista de tarefas.

## Como Executar

para executar basta instalar o Flask usando:

pip install Flask

## Como Funciona

**Estrutura Básica:**
   - O código segue a arquitetura monolito
   - a lógica de negócios está em `app.py`.
   - A interface do usuário é definida no template HTML `templates/index.html`.

**Rotas e Funcionalidades:**
   - A rota principal (`/`) exibe a lista de tarefas.
   - inclusão tarefas: Os usuários podem adicionar novas tarefas através de um formulário.
   - Exclusão de tarefas: Cada tarefa tem um botão para excluí-la.