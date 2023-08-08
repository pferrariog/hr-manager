#!/bin/sh

python manage.py migrate --no-input
python manage.py collectstatic

exec "$@"
# gunicorn app.manager.wsgi:application --bind 0.0.0.0:8000
