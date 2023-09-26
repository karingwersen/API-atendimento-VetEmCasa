#!/bin/bash

service postgresql start

sed -i "s/myPassword/$POSTGRES_PASS/g" /tmp/sql-01.sql

su postgres -c "psql -U postgres -a -f /tmp/sql-01.sql"

python3 api.py