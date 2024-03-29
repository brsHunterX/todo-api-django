# ToDo API

A ToDo API created in Python and Django Rest Framework for case study.

![Badge](https://img.shields.io/static/v1?label=version&message=1.0&color=orange)
![Badge](https://img.shields.io/github/stars/brsHunterX/todo-api-django)

[![Run in Insomnia}](https://insomnia.rest/images/run.svg)](https://insomnia.rest/run/?label=ToDo%20API&uri=https%3A%2F%2Fgithub.com%2FbrsHunterX%2Ftodo-api-django%2Fblob%2Fmain%2Finsomnia.json)

## Instalation

First create a venv

```bash
cd todo-api-django && python3 -m venv ./venv
```

Enable venv in your terminal

```bash
source venv/bin/activate
```

Install requirements

```bash
poetry install
```

Run project migrations

```bash
poetry run python manage.py migrations
```

Launch project

```bash
poetry run python manage.py runserver
```
