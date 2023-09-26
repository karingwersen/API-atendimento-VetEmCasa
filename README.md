# API de atendimento do VetEmCasa

## Requisitos

- Python 3.11
- PostgreSQL 15.2

## Como executar

### Utilizando a máquina local apenas

1. No pgadmin, execute os comandos presentes no arquivo sql-01.sql para criar a estrutura do banco;

2. Usando o pip, instalar as dependências presentes no arquivo requirements.txt (pip install -r requirements.txt);

3. Defina uma variável de ambiente no seu sistema chamada POSTGRES_PASS com o valor de sua senha de acesso ao PostgreSQL;

4. Dentro da pasta app, execute a aplicação rodando o comando python api.py ou python3 api.py; 

### Utilizando Docker

1. Crie localmente a imagem da API de Atendimento executando o comando `docker build -t vetemcasa-api-atendimentos .`;

2. Rode a API executando o comando `docker run -d -p 5000:5000 -e "POSTGRES_PASS=password" --net=bridge vetemcasa-api-atendimentos`. Caso deseje, lembre de substituir o valor da senha do PostgreSQL.

Para ambos os casos, a API será executada no endpoint http://localhost:5000. Seu swagger pode ser encontrado no endpoint http://localhost:5000/swagger.
