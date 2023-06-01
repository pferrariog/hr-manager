
# TODO - Description

...

## Requirements

- Python 3.10+
- Docker 23.0+

## Usage

- Create configuration files

  > - This project uses [Dynaconf](https://www.dynaconf.com/flask/) as management tool/library, so checkout their documentation for more details

  - settings.toml - Here goes project configuration
  - .secrets.toml - Here goes enviroment secrets
  - .env - Here goes your flask configurations

- Build the image and run the container

```sh
    docker build -t $IMAGE_NAME .
    docker run -d -p 80:80 --name $CONTAINER_NAME $IMAGE_NAME
```

## TODO

...
