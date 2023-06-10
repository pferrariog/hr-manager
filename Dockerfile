FROM python:3.11.3
LABEL maintainer="pdrferrari08@gmail.com"

WORKDIR /app

RUN pip install poetry==1.4.0

COPY . .

RUN poetry install --without dev --no-cache --no-interaction

EXPOSE 443

RUN chmod +x /app/docker-entrypoint.sh

CMD ["./docker-entrypoint.sh"]
