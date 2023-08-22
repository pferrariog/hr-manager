FROM python:3

WORKDIR /app

RUN pip install poetry==1.4.0

COPY ./app .

COPY poetry.toml .

COPY docker-entrypoint.sh .

COPY pyproject.toml .

RUN poetry install --without dev --no-cache --no-interaction

RUN chmod +x /app/docker-entrypoint.sh

EXPOSE 8000

CMD ["./docker-entrypoint.sh"]
