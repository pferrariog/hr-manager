
# HR Manager

An multi-tenant app to manage human resources into a company

## Requirements

- Python 3.10+
- Docker 23.0+

## Usage

- Create configuration files

  > - This project uses [Dynaconf](https://www.dynaconf.com/) as management tool/library, so checkout their documentation for more details

  - settings.toml - Here goes project configuration
  - .secrets.toml - Here goes enviroment secrets
  - .env - Here goes your flask configurations

- Build images and run container with compose

```sh
    docker compose up --build
```

## TODO

- Multi-database
- Improve templates
- Add to domain
- Add dynaconf or other settings management tool
