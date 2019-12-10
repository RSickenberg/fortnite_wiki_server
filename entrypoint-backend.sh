#!/bin/bash

pip install -r requirements/base.txt
ls -la /code/

#while ! (echo > /dev/tcp/db/5432) ; do echo -n '.'; sleep 1; done;
echo "Running migrations ..."
./manage.py migrate

echo "Creating admin account ..."
./manage.py loaddata initial_users

echo "Fixturize the env ..."
./manage.py fixturize -y -s --no-reset


exec "${@}"