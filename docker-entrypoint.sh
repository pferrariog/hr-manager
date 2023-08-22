#!/bin/sh

poetry run python manage.py migrate --no-input
# poetry run python manage.py collectstatic --no-input

# exec poetry run gunicorn app.manager.wsgi:application --bind 0.0.0.0:8000
poetry run python manage.py runserver 0.0.0.0:8000 --noreload
