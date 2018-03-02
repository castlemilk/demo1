#!/usr/bin/env bash

until cd demo
do
    echo "Waiting for django volume..."
done

until python manage.py migrate --settings=demo.settings.docker
do
    echo "Waiting for postgres ready..."
    sleep 2
done
python manage.py collectstatic --no-input --settings=demo.settings.docker
python manage.py loaddata fixtures.json --settings=demo.settings.docker
python manage.py runserver 0.0.0.0:8000 --settings=demo.settings.docker

