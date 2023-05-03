# API de atendimento do VetEmCasa

## Requisitos

- Python 3.11
- PostgreSQL 15.2

## Como executar

1. No pgadmin, execute os comandos presentes no arquivo sql-01.sql para criar a estrutura do banco;

2. Usando o pip, instalar as dependências presentes no arquivo requirements.txt (pip install -r requirements.txt);

3. Dentro da pasta app, dentro da pasta controller, no arquivo AtendimentoController.py, adicione sua senha do usuário postgres às linhas 9, 26 e 36;

4. Dentro da pasta app, execute a aplicação rodando o comando python api.py ou python3 api.py. 

A API será executada no endpoint http://localhost:5000. Seu swagger pode ser encontrado no endpoint http://localhost:5000/swagger.