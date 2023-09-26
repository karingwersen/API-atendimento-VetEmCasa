FROM python:3.11

ENV POSTGRES_PASS=password

COPY requirements.txt ./requirements.txt

RUN mkdir /app

COPY ./app /app/

COPY ./sql-01.sql /tmp/sql-01.sql

COPY ./container_startup_script.sh /tmp/container_startup_script.sh

RUN chmod +x /tmp/container_startup_script.sh

RUN python3 -m pip install -r requirements.txt

RUN apt update -y && apt install -y postgresql postgresql-contrib

WORKDIR /app

ENTRYPOINT [ "/tmp/container_startup_script.sh" ]