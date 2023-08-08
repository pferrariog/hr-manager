#!/bin/sh

set -o errexit

python manage.py collectstatic --no-input
python manage.py migrate --no-input

gunicorn app.manager.wsgi:application --bind 0.0.0.0:8000
